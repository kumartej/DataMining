from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import numpy as np

import pandas as pd
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
################## Remove NULL Values
f = f[f.Name.notnull()]
f = f[f.Genre.notnull()]
f = f[f.Year_of_Release.notnull()]
f = f[f.Publisher.notnull()]
print(f.isnull().sum())

################## Encoding

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
# le5 = preprocessing.LabelEncoder()
# le5.fit(f['Developer'].unique())
# f['Developer'] = le5.transform(f['Developer'])
# le6 = preprocessing.LabelEncoder()
# le6.fit(f['Rating'].unique())
# f['Rating'] = le6.transform(f['Rating'])

colRound = ['Critic_Score','Critic_Count','User_Score','User_Count']

############# Round The Float Values
for j in colRound:
	t=[]
	for i in f[j]:
		t.append(round(i))
	f[j]=t


############# Fill Missing Values
ftrain = f.dropna()
ftest = f[f.isnull().any(axis=1)]
ftrainData = ftrain[['Name', 'Platform','Year_of_Release','Publisher', 'Genre', 'NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]

colPredict = ['Critic_Score','Critic_Count','User_Score','User_Count','Developer','Rating']
colInput = ['Name', 'Platform','Year_of_Release','Publisher', 'Genre', 'NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']

fCriticNull = ftest[ftest.Critic_Score.isnull()]
fCriticNonNull = ftest[ftest.Critic_Score.notnull()]
fTrainClass = ftrain['Critic_Score']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fCriticNull[colInput])
fCriticNull['Critic_Score']=t2;

fCombineCritic=[fCriticNull,fCriticNonNull]
ftest = pd.concat(fCombineCritic)

fNull = ftest[ftest.Critic_Count.isnull()]
fNotNull = ftest[ftest.Critic_Count.notnull()]
fTrainClass = ftrain['Critic_Count']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fNull[colInput])
fNull['Critic_Count']=t2
fCombine = [fNull,fNotNull]
ftest = pd.concat(fCombine)

fNull = ftest[ftest.User_Score.isnull()]
fNotNull = ftest[ftest.User_Score.notnull()]
fTrainClass = ftrain['User_Score']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fNull[colInput])
fNull['User_Score']=t2
fCombine = [fNull,fNotNull]
ftest = pd.concat(fCombine)

fNull = ftest[ftest.User_Count.isnull()]
fNotNull = ftest[ftest.User_Count.notnull()]
fTrainClass = ftrain['User_Count']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fNull[colInput])
fNull['User_Count']=t2
fCombine = [fNull,fNotNull]
ftest = pd.concat(fCombine)

fNull = ftest[ftest.Developer.isnull()]
fNotNull = ftest[ftest.Developer.notnull()]
fTrainClass = ftrain['Developer']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fNull[colInput])
fNull['Developer']=t2
fCombine = [fNull,fNotNull]
ftest = pd.concat(fCombine)

fNull = ftest[ftest.Rating.isnull()]
fNotNull = ftest[ftest.Rating.notnull()]
fTrainClass = ftrain['Rating']
clf=GaussianNB()
clf.fit(ftrainData,fTrainClass)
t2 = clf.predict(fNull[colInput])
fNull['Rating']=t2
fCombine = [fNull,fNotNull]
ftest = pd.concat(fCombine)

fCombine = [ftrain,ftest]
f=pd.concat(fCombine)

f['Name'] = le1.inverse_transform(f['Name'])
f['Platform'] = le2.inverse_transform(f['Platform'])
f['Genre'] = le3.inverse_transform(f['Genre'])
f['Publisher'] = le4.inverse_transform(f['Publisher'])
f.to_csv('videoGamesWithNoNulls.csv',index=False)

print(f.isnull().sum())