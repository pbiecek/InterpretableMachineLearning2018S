
import torch
from torch import nn
import torch.nn.functional as F

class ScoreModel(nn.Module):
    def __init__(self, bucketing_model, score_input_dim):
        super().__init__()

        self.bucketing_model = bucketing_model

        self.score_in = nn.Linear(score_input_dim + 1, 50)
        self.relu1 = nn.ReLU()
        self.score_hidden_1 = nn.Linear(50, 50)
        self.relu2 = nn.ReLU()
        self.score_hidden_2 = nn.Linear(50, 50)
        self.relu3 = nn.ReLU()
        self.score_out = nn.Linear(50, 1)

        self.norm = nn.Sigmoid()

    def forward(self, X_bucketing, X_score):

        bucket = self.bucketing_model(X_bucketing)
        score = torch.cat([bucket, X_score], dim=1)

        score = self.score_in(score)
        score = self.relu1(score)
        score = self.score_hidden_1(score)
        score = self.relu2(score)
        score = self.score_hidden_2(score)
        score = self.relu3(score)
        score = self.score_out(score)
        score = self.norm(score)

        return score

class BucketingModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        
        self.input_dim = input_dim
        self.bucketing_in = nn.Linear(input_dim, 30)
        self.relu1 = nn.ReLU()
        self.bucketing_out = nn.Linear(30, 1)
        self.norm = nn.Sigmoid()

    def forward(self, X_bucketing):
        bucket = self.bucketing_in(X_bucketing)
        bucket = self.relu1(bucket)
        bucket = self.bucketing_out(bucket)
        bucket = self.norm(bucket)
        return bucket