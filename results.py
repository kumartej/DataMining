# from sklearn import preprocessing
# import numpy as np
import pandas as pd
# import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
print(f.isnull().sum())
f=f.dropna()


platform_tol_sales=f.groupby(['Year_of_Release','Platform'])['Global_Sales'].sum()
temp = platform_tol_sales.unstack().plot()
plt.title('Year Of Relase Platform Global Sales')
plt.ylabel('Global Sales')
plt.show()

df_count=f.groupby(['Publisher'])['Platform'].count()
_df_count=df_count.sort_values(ascending=False).head(10)
_df_count.plot(kind='bar')
plt.title('Publisher Platform Count')
plt.xlabel('Publisher')
plt.show()

# df1['User_Score']=pd.to_numeric(df1['User_Score'])
pubUser = f.groupby(['Publisher'])['User_Score'].sum().sort_values(ascending=False).head(10)
pubUser.plot(kind='bar')
plt.title('Publisher User Score')
plt.xlabel('Publisher')
# plt.show()