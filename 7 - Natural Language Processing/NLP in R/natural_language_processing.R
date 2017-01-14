#NLP 

#importing the dataset
dataset = read.delim('Restaurant_Reviews.tsv',quote = '',stringsAsFactors = FALSE)

#cleaning the texts
# install.packages('tm')
library(tm)
corpus = VCorpus(VectorSource(dataset$Review))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)

