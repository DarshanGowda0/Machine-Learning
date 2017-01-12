# -*- coding: utf-8 -*-
#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

#finding the optimal number of clusters using the dendrogram
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X,method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidian Distance')
plt.show()

#optimal number of clusters obtained is 5
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

#visualising the result 
plt.scatter(X[y_hc == 0,0],X[y_hc == 0,1],s = 100, c = 'red', label = 'Careful')
plt.scatter(X[y_hc == 1,0],X[y_hc == 1,1],s = 100, c = 'blue', label = 'Standard')
plt.scatter(X[y_hc == 2,0],X[y_hc == 2,1],s = 100, c = 'green', label = 'Target')
plt.scatter(X[y_hc == 3,0],X[y_hc == 3,1],s = 100, c = 'cyan', label = 'Careless')
plt.scatter(X[y_hc == 4,0],X[y_hc == 4,1],s = 100, c = 'magenta', label = 'Sensible')
plt.title('Cluster of Clients')
plt.xlabel('income')
plt.ylabel('spend')
plt.legend()
plt.show()