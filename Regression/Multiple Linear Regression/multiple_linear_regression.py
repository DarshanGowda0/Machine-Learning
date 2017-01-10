# -*- coding: utf-8 -*-

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#####encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#for encoding the text into single digit numbers
labelEncoder_X = LabelEncoder()
X[:, 3] = labelEncoder_X.fit_transform(X[:, 3])

#for encoding text into binary digits, so that the ML algorithms dont take them into consideration
#(usually done for independent variables)
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#removing dummy trap
X = X[:, 1:]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting multiple linear regression to training data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#predicting the results for multiple linear regression using the test data
y_pred = regressor.predict(X_test)
