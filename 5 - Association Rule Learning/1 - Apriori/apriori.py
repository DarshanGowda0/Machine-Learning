# -*- coding: utf-8 -*-

#we are making use of the apyori class stored in the same directory, which is a clone from its official library

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset 
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0,7501):
    print(i)
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
#training apriori on dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
 
results = list(rules)
myResults = [list(x) for x in results] 
