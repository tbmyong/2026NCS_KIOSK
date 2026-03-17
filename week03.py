import numpy as np
import pandas as pd #pandas는 labeling이 가능하다

items = {'a': [100, 80, 90],
         'b': [95, 75, 85],
         'c': [10, 80, 90]
         }

df_items = pd.DataFrame(items, index=[1,2,3])
print(df_items)


items = [
    [100, 95, 10],
    [80, 75, 80],
    [90, 85, 90]
]

df_items = pd.DataFrame(items, index=[1,2,3], columns=['a','b','c'])
print(df_items)
df_items_melt = pd.melt(df_items).rename(columns={'variable':'var','value':'val'}).query('val >= 85')
print(df_items_melt)

