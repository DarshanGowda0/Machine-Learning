

#importing the dataset
dataset = read.csv('Data.csv')

#taking care of the missing data
#if null, then take average else leave the same
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

#encoding categorical data
#we use factors by default in R unlike python
dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes','No'),
                           labels = c(1,0))

#splitting the datasets into train and test datasets

#install package 
#install.packages('caTools')

#import library 
library('caTools')
#genrate a random number
set.seed(123)
#use sample.split from caTools to split 
split  = sample.split(dataset$Purchased, SplitRatio = 0.8)

#make the subsets using the split
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset, split == FALSE)


