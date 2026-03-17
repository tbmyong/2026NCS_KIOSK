import numpy as np
import pandas as pd #pandas는 labeling이 가능하다

items = {'a': [100, 80, 90],
         'b': [95, 75, 85],
         'c': [10, 80, 90]
         }

df_items = pd.DataFrame(items, index=[1,2,3])
print(df_items)