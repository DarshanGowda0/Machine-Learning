# -*- coding: utf-8 -*-
#import all the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data preprocessing
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#dont split the data, minimal data available

#no feature scaling as well

#simple linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly ,y)

