import pandas as pd
f = pd.read_csv('videoGamesWithNoNulls.csv')
print(f.isnull().sum())
NA_Sales = f['NA_Sales']
print(NA_Sales.min(),NA_Sales.max())
bins = [-100,0, 10, 20, 30, 40, 50,100]
group_names = ['poor','veryLow', 'low', 'medium', 'high', 'veryHigh','excellent']
f['NA_Sales'] = pd.cut(f['NA_Sales'], bins, labels=group_names)
f['EU_Sales'] = pd.cut(f['EU_Sales'], bins, labels=group_names)
f['JP_Sales'] = pd.cut(f['JP_Sales'], bins, labels=group_names)
f['Global_Sales'] = pd.cut(f['Global_Sales'], bins, labels=group_names)
bins = [-1,3,6,9,12]
group_names = ['Poor','Low','Medium','High']
f['Other_Sales'] = pd.cut(f['Other_Sales'], bins, labels=group_names)
bins = [0,20,40,60,80,100]
group_names = ['Poor','Low','Medium','High','Excellent']
f['Critic_Score'] = pd.cut(f['Critic_Score'], bins, labels=group_names)
print(f)