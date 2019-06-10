import pandas as pd
import numpy as np
import yaml
import logging
import os
from datetime import datetime
import time
from shutil import copyfile
import shutil
import argparse
import utils_.helpers as helpers
from models.baseline import BucketingModel, ScoreModel

import torch
import torch.nn.functional as F
from torch import nn
from torch import optim
import utils_.learning as torch_utils
from torch.utils.data import TensorDataset

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    log_loss,
    accuracy_score,
    classification_report,
    roc_curve,
    auc,
    roc_auc_score,
)
import random
from sklearn.preprocessing import MinMaxScaler

random.seed(24)


def show_score(y, y_pred):
    fpr, tpr, threshold = roc_curve(y.astype("int"), y_pred)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, "blue", label=f"AUC = {roc_auc}")

    plt.title("Receiver Operating Characteristic")
    plt.legend(loc="lower right")
    plt.plot([0, 1], [0, 1], "r--")
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    #plt.show()
    plt.savefig('score.png')


X = pd.read_csv(f"datasets/Xk.csv", sep=";")
for col in X.columns:
    X[col] = MinMaxScaler().fit_transform(X[col].values.reshape(-1,1))

X.head(10)


X_bucketing = X[
    [
        "population",
        "buty",
        "ubrania",
        "torebki",
        "salary",
        "marketingChannel_Organic Search",
        "marketingChannel_Paid Search",
        "marketingChannel_Retargeting",
        "device_desktop",
        "device_mobile",
        "device_tablet",
    ]
]
X_score = X[
    [
        "price",
        "discountPercent"
    ]
]
y = X[["y"]]

split_idx = int(len(y) * 0.8)
split = split_idx * ["train"] + (len(y) - split_idx) * ["valid"]
split = np.random.permutation(split)

bucketing_model = BucketingModel(X_bucketing.shape[1])
model = ScoreModel(bucketing_model, X_score.shape[1])

logging.basicConfig(filename=f"logs.txt", level=logging.DEBUG)

# setting device on GPU if available, else CPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
logging.info(f"Using device: {device}")
logging.info("")

# Additional Info when using cuda
if device.type == "cuda":
    logging.info(torch.cuda.get_device_name(0))
    logging.info("Memory Usage:")
    logging.info(f"Allocated: {round(torch.cuda.memory_allocated(0)/1024**3,1)}GB")
    logging.info(f"Cached: {round(torch.cuda.memory_cached(0)/1024**3,1)}GB")

def get_tensor_dataset(d_split=None):
    if d_split is None:
        s = [True] * len(split)
    else:
        s = split == d_split

    return TensorDataset(
        torch.Tensor(X_bucketing.values[s]).to(device),
        torch.Tensor(X_score.values[s]).to(device),
        torch.Tensor(y.values[s]).to(device),
    )


model = model.to(device)
batch_size = 4096

dataset = get_tensor_dataset()
dataset_train = get_tensor_dataset("train")
dataset_valid = get_tensor_dataset("valid")

train_dl, valid_dl = torch_utils.get_data(dataset_train, dataset_valid, batch_size)

loss = nn.BCELoss()
opt = optim.Adam(model.parameters(), lr=0.001)
epochs = 10

train_loss, val_loss = torch_utils.fit(epochs, model, loss, opt, train_dl, valid_dl)
torch.save(model.state_dict(), "model.1.pth")

with torch.no_grad():
    buckets = bucketing_model.forward(dataset.tensors[0])
    buckets = buckets.to("cpu").data.numpy()
    buckets_df = pd.DataFrame({"bucket": buckets.reshape((-1))})
    buckets_df.to_csv(f"buckets.csv", index=False, sep=";")
    score = model.forward(dataset_valid.tensors[0], dataset_valid.tensors[1])
    score = score.to("cpu").data.numpy()
    show_score(dataset_valid.tensors[2].to("cpu").data.numpy(), score)


