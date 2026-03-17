import  numpy as np
#import pandas as pd

data = np.array([40, 30, 20, 10], dtype=float)
#data = np.array([40, 30.0, 20, 10])
#중간에 30.0으로 해서 하나만 float type을 넣은 경우 C에서는 안되나 python에서는 가능
#python에서 float로 처리함
print(data)

data2 = np.array([[1,2],[3,4]])
print(data2)

data3 = np.zeros((3,4,2))  #zeros-모든 요소를 0으로 채운 배열 생성
print(data3)

data4 = np.ones((8))  #ones-모든 요소를 1으로 채운 배열 생성
print(data4)

#np.rand.rand():0~1사이의 균등 분포에서 난수 생성 np.rand.randn():표준정규분포에서 난수 생성

#arange, full, np.random.rand(), linspace


print(data.dtype, data2.dtype,data3.dtype,data4.dtype)
print(data.shape, data2.shape,data3.shape,data4.shape)