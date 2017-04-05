# from sklearn import preprocessing
import numpy as np
import pandas as pd
# import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
print(f.isnull().sum())
f=f.dropna()
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
# ax.hist(f['Year_of_Release'],bins = 7)
# plt.title('Trail Graph')
# plt.xlabel('Year')
# plt.ylabel('XXX')
# plt.show()

# ax.scatter(f['Year_of_Release'],f['EU_Sales'])
# # plt.show()

# var = f.groupby('Year_of_Release').EU_Sales.mean()
# ax.set_xlabel('Year Of Release')
# ax.set_ylabel('mean of EU_Sales')
# ax.set_title('Year of Release Vs Mean of EU_Sales')
# var.plot(kind='bar')
# plt.show()

# sns.boxplot(data=f, x="Year_of_Release", y="EU_Sales")
# sns.plt.show()

removeRat = ['AO','EC', 'K-A','RP']
mask = np.logical_not(f['Rating'].isin(removeRat))
f=f[mask]

sns.boxplot(data=f, x="Rating", y="Critic_Score")
sns.plt.show()

sns.boxplot(data=f, x="Platform", y="Critic_Score")
sns.plt.show()

fsub = f[f.Year_of_Release.notnull()]
sns.barplot(x="Year_of_Release",y="EU_Sales",data=fsub)
sns.plt.show()
sns.barplot(x="Year_of_Release",y="JP_Sales",data=fsub)
sns.plt.show()
sns.barplot(x="Year_of_Release",y="NA_Sales",data=fsub)
sns.plt.show()

sns.barplot(x="Genre",y="Global_Sales",data=fsub)
sns.plt.show()

video = f
video7th = video

# yearlySales = video7th.groupby(['Year_of_Release','Platform']).Global_Sales.sum()
# yearlySales.unstack().plot(kind='bar',stacked=True, colormap= 'Blues',  grid=False)
# plt.title('Stacked Barplot of Global Yearly Sales of the 7th Gen Consoles')
# plt.ylabel('Global Sales')
# plt.show()

# video7th = video[(video['Platform'] == 'Wii') | (video['Platform'] == 'PS3') | (video['Platform'] == 'X360')]

# yearlySales = video7th.groupby(['Year_of_Release','Platform']).Global_Sales.sum()
# yearlySales.unstack().plot(kind='bar',stacked=True, colormap= 'Blues',  grid=False)
# plt.title('Stacked Barplot of Global Yearly Sales of the 7th Gen Consoles')
# plt.ylabel('Global Sales')
# plt.show()

# ratingSales = video7th.groupby(['Rating','Platform']).Global_Sales.sum()
# ratingSales.unstack().plot(kind='bar',stacked=True,  colormap= 'Greens', grid=False)
# plt.title('Stacked Barplot of Sales per Rating type of the 7th Gen Consoles')
# plt.ylabel('Sales')
# plt.show()
