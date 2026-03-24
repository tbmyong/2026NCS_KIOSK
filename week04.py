import pandas as pd
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.info())
#mpg.dropna(subset=['horsepower'], inplace=True) #원본 저장
#print(mpg.info())
mpg_clean = mpg.dropna(subset=['horsepoewr']) #사본 생성
print(mpg_clean)