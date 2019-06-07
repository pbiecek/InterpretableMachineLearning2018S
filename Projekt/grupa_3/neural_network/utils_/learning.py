import numpy as np
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import logging
from datetime import datetime
import time
import utils_.helpers as helpers

def get_loss(model, loss_func, data_loader):
    losses, nums = zip(*[loss_batch(model, loss_func, None, batch[-1], batch[:-1]) for batch in data_loader])
    return np.sum(np.multiply(losses, nums)) / np.sum(nums)

def fit(epochs, model, loss_func, opt, train_dl, valid_dl):
    for epoch in range(epochs):
        start_time = time.time()
        
        model.train()
        for batch in train_dl:
            loss_batch(model, loss_func, opt, batch[-1], batch[:-1])

        model.eval()
        with torch.no_grad():
            train_loss = get_loss(model, loss_func, train_dl)
            val_loss = get_loss(model, loss_func, valid_dl)
        
        logging.info(f"[{helpers.get_timestamp()}] E[{helpers.parse_execution_time(int(time.time() - start_time))}] Epoch {epoch}: {train_loss} ({val_loss})")
    return train_loss, val_loss


def get_data(train_ds, valid_ds, batch_size):
    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=False),
        DataLoader(valid_ds, batch_size=batch_size * 2, shuffle=False),
    )


def loss_batch(model, loss_func, opt, yb, xb):
    loss = loss_func(model(*xb), yb)

    if opt is not None:
        loss.backward()
        opt.step()
        opt.zero_grad()

    return loss.item(), len(xb[0])
