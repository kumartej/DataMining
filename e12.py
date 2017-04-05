import itertools
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import linear_model
from sklearn import svm
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import seaborn as sns
from sklearn.model_selection import cross_val_predict

f=pd.read_csv('videoGamesWithNoNulls.csv')

removeRat = ['AO','EC', 'K-A','RP']
mask = np.logical_not(f['Rating'].isin(removeRat))
f=f[mask]


le1 = preprocessing.LabelEncoder()
le1.fit(f['Name'].unique())
f['Name'] = le1.transform(f['Name'])
le2 = preprocessing.LabelEncoder()
le2.fit(f['Platform'].unique())
f['Platform'] = le2.transform(f['Platform'])
le3 = preprocessing.LabelEncoder()
le3.fit(f['Genre'].unique())
f['Genre'] = le3.transform(f['Genre'])
le4 = preprocessing.LabelEncoder()
le4.fit(f['Publisher'].unique())
f['Publisher'] = le4.transform(f['Publisher'])
le5 = preprocessing.LabelEncoder()
le5.fit(f['Developer'].unique())
f['Developer'] = le5.transform(f['Developer'])

fData = f.drop('Rating',1)
fTest = f['Rating']

rfc = RandomForestClassifier()
scores = cross_val_score(rfc, fData, fTest, cv=5)
print("accuracy::",scores.mean())

predicted = cross_val_predict(rfc, fData, fTest, cv=5)
print("accuracy::",accuracy_score(fTest, predicted))

predicted = cross_val_predict(rfc, fData, fTest, cv=10)
print("accuracy::",accuracy_score(fTest, predicted))