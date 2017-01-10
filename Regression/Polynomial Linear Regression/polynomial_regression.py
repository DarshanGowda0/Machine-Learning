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
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly ,y)

#visualistaions for linear regression model
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#visualisations for polynomial regression model
X_grid = np.arange(max(X), min(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


#predicting a new result with Linear Regression
lin_reg.predict(6.5)

#predicting the new result with Polynomail Linear Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))