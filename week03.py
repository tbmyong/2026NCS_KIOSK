import numpy as np
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(3))
#print(mpg.iloc[:,[0,1]])
#print(mpg.iloc[2:5,[0,1]])
#print(mpg.loc[:,'model_year':'origin'])
print(mpg.iat[1, 8])

