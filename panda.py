# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

sc=pd.Series([84,92,88,95], index=["國文","英文","數學","資訊科技"])
print(sc["數學"])#取出索引
sc["數學"]
sa=[84,92,88,95],["國文","英文","數學","資訊科技"]
print(len(sa)) #陣列個數
for i in range(len(sa[0])):
    print(sa[0][i],sa[1][i])#印出所有陣列
    
data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11,23,8,3,11]}
myframe = pd.DataFrame(data)
print(myframe)

subject=["chinese","english","math","human","science"]
name=["gin","mike","min","gone"]
sorce=[86,88,82,87,92],[92,100,95,99,96],[82,87,86,82,82],[91,92,99,91,92]
df=pd.DataFrame(sorce, name, subject)
print(df)

df["program"]=[100,100,100,100]

print(df)