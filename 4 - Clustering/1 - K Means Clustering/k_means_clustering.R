# import the dataset
dataset <- read.csv('Mall_Customers.csv')
X = dataset[4:5]

#find the optimal number of clusters using the elbow method
set.seed(6)
wcss = vector()
for(i in 1:10) wcss[i] = sum(kmeans(X,i)$withinss)
plot(1:10,wcss,type="b",main = 'elbow method',xlab = 'number of clusters',ylab = 'wcss')

#the optimal number of clusters obtained is 5
set.seed(29)
kmeans = kmeans(X,5,iter.max = 300,nstart = 10)

# install.packages('cluster')
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Cluster of Clients'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')
