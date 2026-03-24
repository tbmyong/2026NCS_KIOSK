import pandas as pd
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.info())
#mpg.dropna(subset=['horsepower'], inplace=True) #원본 저장
#print(mpg.info())
mpg_clean = mpg.dropna(subset=['horsepoewr']) #사본 생성
print(mpg_clean.info())


hp_median = mpg['horsepower'].median()
mpg_filled = mpg.copy()
mpg_filled['horsepower'] = mpg_filled['horsepower'].fillna(hp_median)
print(mpg_filled.info())