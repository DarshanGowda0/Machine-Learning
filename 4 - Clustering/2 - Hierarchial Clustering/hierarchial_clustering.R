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
