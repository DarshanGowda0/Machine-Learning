#importing the dataset as sparse matrix 
# install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv',sep = ',',rm.duplicates = TRUE)
itemFrequencyPlot(dataset,topN = 50)

#training apriori for the dataset 
rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))

#visualising the results
inspect(sort(rules, by = 'lift')[1:10])