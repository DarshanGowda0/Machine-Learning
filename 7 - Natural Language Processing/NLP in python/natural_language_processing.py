# -*- coding: utf-8 -*-

# importing the libraries
import pandas as pd

# importing the dataset, set the delimiter as tab for tsv, quoting to 3 to maintain the quotes
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# cleaning the texts 
import re
from nltk.stem.porter import PorterStemmer
# nltk.download('stopwords')
from nltk.corpus import stopwords
corpus = []

operators = set(('and', 'or', 'not'))
stop = set(stopwords.words('english')) - operators

for i in range(0, 1000):
    # review = review.lower().split()
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]).lower().split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in stop]
    review = ' '.join(review)
    corpus.append(review)
    
#creating bag of words 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)