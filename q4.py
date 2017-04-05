from sklearn import preprocessing
import numpy as np
import pandas as pd
import statistics as st
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
# print(f['NA_Sales'][0])
# print(st.mean(f['NA_Sales']))
# print(st.stdev(f['NA_Sales']))
# mn=st.mean(f['NA_Sales'])
# stdeva=st.stdev(f['NA_Sales'])
# arr=[]
# for i in f['NA_Sales']:
# 	arr.append((i-mn)/stdeva)
# print(arr[0])
# print(f.dtypes)
# print(f[f.isnull().any(axis=1)])
f=f.fillna(0)
X_scaled = preprocessing.scale([f['NA_Sales'],f['EU_Sales'],f['JP_Sales'],f['Other_Sales'],f['Global_Sales'],f['Critic_Score'],f['Critic_Count'],f['User_Score'],f['User_Count']])
X_scaled_round=[]
for i in X_scaled:
	tmp=[]
	tmp=[round(j) for j in i]
	# for j in i:
	# 	tmp.append(round(j))
	X_scaled_round.append(tmp)
print(X_scaled_round)
# for i in X_scaled[0]:
# 	print(i)