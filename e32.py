import itertools
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import svm
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):

	plt.imshow(cm, interpolation='nearest', cmap=cmap)
	plt.title(title)
	plt.colorbar()
	tick_marks = np.arange(len(classes))
	plt.xticks(tick_marks, classes, rotation=45)
	plt.yticks(tick_marks, classes)

	if normalize:
	    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
	    print("Normalized confusion matrix")
	else:
		print('Confusion matrix, without normalization')

	print(cm)

	thresh = cm.max() / 2.
	for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
	    plt.text(j, i, cm[i, j],
	             horizontalalignment="center",
	             color="white" if cm[i, j] > thresh else "black")

	plt.tight_layout()
	plt.ylabel('True label')
	plt.xlabel('Predicted label')


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

msk = np.random.rand(len(f)) < 0.7
train = f[msk]
test = f[~msk]

trainData = train.drop('Rating',1)
trainClass = train['Rating']
testData = test.drop('Rating',1)
testClass = test['Rating']

class_names = f['Rating'].unique()

clf = GaussianNB()
clf.fit(trainData,trainClass)
predNBClass = clf.predict(testData)
acc = accuracy_score(testClass,predNBClass)
cnfMat = confusion_matrix(testClass,predNBClass)
plt.figure()
plot_confusion_matrix(cnfMat,classes=class_names,title='Confusion matrix for Naive Bayesian Classifier')
plt.show()
print(classification_report(testClass,predNBClass, target_names=class_names))
print(acc)

rfc = RandomForestClassifier()
rfc.fit(trainData,trainClass)
predRFClass = rfc.predict(testData)
acc = accuracy_score(testClass,predRFClass)
cnfMat = confusion_matrix(testClass,predRFClass)
plt.figure()
plot_confusion_matrix(cnfMat,classes=class_names,title='Confusion matrix for Random Forest Classifier')
plt.show()
print(classification_report(testClass,predRFClass, target_names=class_names))
print(acc)



svmclf = svm.SVC()
svmclf.fit(trainData,trainClass)
predSvmClass = svmclf.predict(testData)
acc = accuracy_score(testClass,predSvmClass)
cnfMat = confusion_matrix(testClass,predSvmClass)
plt.figure()
plot_confusion_matrix(cnfMat,classes=class_names,title='Confusion matrix for SVM')
plt.show()
print(classification_report(testClass,predSvmClass, target_names=class_names))
print(acc)

