import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


crash_df = sns.load_dataset('car_crashes')
print(crash_df.head())
sns.jointplot(x='speeding',y= 'alcohol',data =crash_df,kind='resid')
plt.show()