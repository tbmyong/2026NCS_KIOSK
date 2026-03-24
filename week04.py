import pandas as pd

def sequaes(n):
    return n * n
items = {
    'a' : [100, 80, 90],
    'b' : [100, 95, 75],
    'c' : [100, 60, 90]
}

df_itmes = pd.DataFrame(items, index=[1,2,3])
#print(df_items)
print(df_itmes.apply(sequaes)) #애는 squares랑 같이 쓰거나 아님 람다만 혼자 씀
print(df_itmes.apply(lambda n : n * n))