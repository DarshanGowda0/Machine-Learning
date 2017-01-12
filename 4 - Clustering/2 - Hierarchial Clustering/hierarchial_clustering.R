#importing dataset 
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

#selecting the optimised number of clusters
dendrogram = hclust(dist(X, method = 'euclidean'), method = 'ward.D')
plot(dendrogram,
     main = paste('Dendrogram'),
     xlab = 'Customers',
     ylab = 'Euclidean distances')

#fitting hierarchial clustering using 5 clusters 
hc = hclust(dist(X, method = 'euclidean'), method = 'ward.D')
y_hc = cutree(hc, 5)


#visualisation of clusters in hierarchial clustering
# install.packages('cluster')
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Cluster of Clients'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')
