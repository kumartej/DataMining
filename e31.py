import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import svm

f=pd.read_csv('videoGamesWithNoNulls.csv')

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

msk = np.random.rand(len(f)) < 0.7
train = f[msk]
test = f[~msk]

trainData = train.drop('Rating',1)
trainClass = train['Rating']
testData = test.drop('Rating',1)
testClass = test['Rating']

clf = GaussianNB()
clf.fit(trainData,trainClass)
predNBClass = clf.predict(testData)
acc = accuracy_score(testClass,predNBClass)
print(acc)

rfc = RandomForestClassifier()
rfc.fit(trainData,trainClass)
predRFClass = rfc.predict(testData)
acc = accuracy_score(testClass,predRFClass)
print(acc)

le6 = preprocessing.LabelEncoder()
le6.fit(f['Rating'].unique())
trainClass = le6.transform(trainClass)
testClass = le6.transform(testClass)

reg = linear_model.LinearRegression()
reg.fit(trainData,trainClass)
predRegClass = rfc.predict(testData)
acc = accuracy_score(testClass,predRegClass)
print(acc)

trainClass = le6.inverse_transform(trainClass)
testClass = le6.inverse_transform(testClass)

svmclf = svm.SVC()
svmclf.fit(trainData,trainClass)
predSvmClass = svmclf.predict(testData)
acc = accuracy_score(testClass,predSvmClass)
print(acc)