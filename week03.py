import numpy as np

items = [40, 7, 99, -3]
items_new = []
for item in items:
    items_new.append(item + 5)
print(items_new)


items = [40, 7, 99, -3]
items =list(map(lambda i: i+5, items))
print(items)

#위와 결과 동일 모든 값에 +5되어 출력된다
#data1 = np.array([40, 7, 99, -3])
#print(data1 + 5)

