import numpy as np
import pandas as pd

from subprocess import check_output

from IPython.display import display, HTML

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

import seaborn as sns

vg_df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
vg_df.User_Score = vg_df.User_Score.convert_objects(convert_numeric=True)
temp1 = vg_df.groupby(['Year_of_Release']).count()
temp1 = temp1.reset_index()

temp2 = vg_df.groupby(['Year_of_Release']).sum()
temp2 = temp2.reset_index()
normalised_df = pd.DataFrame()

normalised_df['release_count'] = temp1['Name']
normalised_df['global_sales'] = temp2['Global_Sales']
normalised_df = (normalised_df - normalised_df.mean()) / normalised_df.std()
normalised_df['year'] = temp1['Year_of_Release']

plt.figure(figsize=(15, 9))
ax = sns.pointplot(x = normalised_df.year, y = normalised_df.release_count, color = 'blue', label='Release Count')
ax = sns.pointplot(x = normalised_df.year, y = normalised_df.global_sales, color = 'red', label='Global Sales')

blue_patch = mpatches.Patch(color='blue', label='NUMBER OF RELEASES')
red_patch = mpatches.Patch(color='red', label='GLOBAL SALES')
plt.legend(handles=[blue_patch, red_patch], loc='upper left', fontsize = 16)

plt.xticks(rotation=45);
plt.show()
