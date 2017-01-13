# -*- coding: utf-8 -*-

# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset, set the delimiter as tab for tsv, quoting to 3 to maintain the quotes
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# cleaning the texts 
import re
import nltk
from nltk.stem.porter import PorterStemmer
# nltk.download('stopwords')
from nltk.corpus import stopwords
corpus = []

for i in range(0, 1000):
    # review = review.lower().split()
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]).lower().split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
    
    
