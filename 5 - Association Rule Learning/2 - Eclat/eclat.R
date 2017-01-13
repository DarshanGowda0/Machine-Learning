#importing the dataset as sparse matrix 
# install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv',sep = ',',rm.duplicates = TRUE)
itemFrequencyPlot(dataset,topN = 50)

#training apriori for the dataset 
rules = eclat(data = dataset, parameter = list(support = 0.004, minlen = 2))

#visualising the results
inspect(sort(rules, by = 'support')[1:10])