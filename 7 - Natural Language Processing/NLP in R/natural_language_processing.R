#NLP 

#importing the dataset
dataset = read.delim('Restaurant_Reviews.tsv',quote = '',stringsAsFactors = FALSE)

#cleaning the texts
# install.packages('tm')
# install.packages("SnowballC")
library(tm)
library(SnowballC)
corpus = VCorpus(VectorSource(dataset$Review))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords())
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, stripWhitespace)




