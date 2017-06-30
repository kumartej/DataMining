import pandas as pd
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
# print(f)
# ar2=[]
# for line in f:
# 	ar2.append([x.strip() for x in line.split(',')])
# print(ar2)
tot=len(f)
count=f.isnull().sum()/tot*100
print(count)
print(count)
print(count)
