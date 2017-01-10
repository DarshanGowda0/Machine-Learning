# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')

#all rows and all columns except last (matrix)
X = dataset.iloc[:, :-1].values

#all rows and 1st indexed cloumn (vector)
y = dataset.iloc[:, 1].values

# Splitting the dataset into 20 rows for training and 10 for test data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling is not required for simple linear regression
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting the regression to training data
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train,y_train)

#predicting the test set results 
y_pred = regression.predict(X_test)

#visualising the results by plotting graphs

#scatter all the training data in red color
plt.scatter(X_train, y_train, color = 'red')
#plot the regression line for the training data
plt.plot(X_train, regression.predict(X_train), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#scatter all the test data in red color
plt.scatter(X_test, y_test, color = 'red')
#plot the regression line for the training data
plt.plot(X_train, regression.predict(X_train), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Predicted Salary')
plt.show()