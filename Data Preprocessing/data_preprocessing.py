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

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#for encoding the text into single digit numbers
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])

#for encoding text into binary digits, so that the ML algorithms dont take them into consideration
#(usually done for independent variables)
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

#use label encoder for y, because its a dependant variable
labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)

#seperating the training and test data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_trian, y_test = train_test_split(X, y, test_size= 0.2, random_state = 0)