import numpy as np

import pandas as pd
f=pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
print(f.info())
StrColumns = ['Name','Platform','Genre','Publisher','Developer','Rating']
for i in StrColumns:
	f[i]=f[i].str.replace(',','')
	f[i]=f[i].str.replace("'",'')
	f[i]=f[i].str.replace(":",'')
	f[i]=f[i].str.replace("%",'')
f.to_csv('remove_commas.csv',index=False)
f=pd.read_csv('videoGamesWithNoNulls.csv')
print(f.info())