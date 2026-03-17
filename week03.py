import numpy as np
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(3))
print(mpg.tail(3))
print(mpg.query('mpg>27.0'))

mpg_asc = mpg.sort_values('mpg')
print(mpg_asc)
msg_asc_disp_out = mpg_asc.drop(columns=['displacement'])
print(msg_asc_disp_out)