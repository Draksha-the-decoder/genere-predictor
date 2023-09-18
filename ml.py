import numpy as np
from sklearn.datasets import fetch_20newsgroups
newsgroups=fetch_20newsgroups()
#defining all categories
categories =['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
train = fetch_20newsgroups(subset='train',categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

#creating the model
model=make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(train.data, train.target)

predicted= model.predict(test.data)
from sklearn.metrics import confusion_matrix
mat= confusion_matrix(test.target,predicted)
from sklearn.metrics import accuracy_score
print("Accuracy",accuracy_score(test.target,predicted))

import pickle
pickle.dump(model,open('model.pkl','wb'))