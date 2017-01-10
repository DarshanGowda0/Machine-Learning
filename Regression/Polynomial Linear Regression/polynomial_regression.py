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


