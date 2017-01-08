# -*- coding: utf-8 -*-

#required imports 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Data.csv')

#get all columns except last
X = dataset.iloc[:,:-1].values

#get the third indexed column
y = dataset.iloc[:,3].values

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

