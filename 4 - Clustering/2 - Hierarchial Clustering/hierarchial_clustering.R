#importing dataset 
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

#selecting the optimised number of clusters
dendrogram = hclust(dist(X, method = 'euclidean'), method = 'ward.D')
plot(dendrogram,
     main = paste('Dendrogram'),
     xlab = 'Customers',
     ylab = 'Euclidean distances')