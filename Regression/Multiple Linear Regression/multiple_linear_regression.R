#data preprocessing 
dataset = read.csv('50_startups.csv')

#encoding categorical data
dataset$State = factor(dataset$State,
                       levels = c('California','New York','Florida'),
                       labels = c(1,2,3))

#splitting the dataset in training and test data
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#feature scaling is not required

