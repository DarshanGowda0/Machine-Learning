#importing dataset 
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[, 3:5]

# splitting the data into training set and test set
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased,SplitRatio = 0.75)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

#feature scaling of independant variables
training_set[, 1:2] = scale(training_set[, 1:2])
test_set[, 1:2] = scale(test_set[, 1:2])

#fitting the classifier
classifier = glm(formula = Purchased ~ .,
                 family = 'binomial',
                 data = training_set)
