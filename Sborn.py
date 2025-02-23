#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


crash_df = sns.load_dataset('car_crashes')
print(crash_df.head())
sns.jointplot(x='speeding',y= 'alcohol',data =crash_df,kind='resid')
plt.show()
#Joint Plot

#plot_kinds = ["scatter", "hist", "hex", "kde", "reg", "resid"]
sns.jointplot(x='speeding',y= 'alcohol',data =crash_df,kind='resid')

#KDE PLOT
sns.kdeplot(crash_df['alcohol'])

# Pair Plot
#sns.pairplot(crash_df)
tips_df= sns.load_dataset('tips')
#tips_df.plot()
sns.pairplot(tips_df,hue='sex',palette='Reds')

#Rug Plot
tips_df= sns.load_dataset('tips')
sns.rugplot(tips_df['total_bill'])

