import pandas as pd
import numpy as np

train_dataset = pd.read_csv('C:/Users/tomas/OneDrive/Documents/Studies/PW-IAD/WUM/train.csv')
test_dataset = pd.read_csv('C:/Users/tomas/OneDrive/Documents/Studies/PW-IAD/WUM/test.csv')

# 2 lata, 3 klasa, 3 rodzenstwa, 1 rodzic, kobieta, 10 GBP
train_dataset = train_dataset[['Age','Pclass','SibSp','Parch','Sex','Fare','Survived']].dropna()
train = train_dataset[['Age','Pclass','SibSp','Parch','Sex','Fare']]
labels = train_dataset['Survived']
train = train.replace('male',0).replace('female',1)

test_dataset = test_dataset[['Age','Pclass','SibSp','Parch','Sex','Fare']].dropna()
test = test_dataset[['Age','Pclass','SibSp','Parch','Sex','Fare']]
test = test.replace('male',0).replace('female',1)

from sklearn.ensemble import RandomForestClassifier
model_rf = RandomForestClassifier(n_estimators = 10000, max_depth = 5, random_state = 0)
model_rf.fit(train, labels)
model_rf.predict_proba([[2, 3, 3, 1, 0, 10]])

# Pawdopodobieństwo że przeżyje wynosi 0.37