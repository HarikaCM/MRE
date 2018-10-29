# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:10:48 2018i i

@author: Harika
"""


import pandas as pd
import numpy as np
scores = pd.read_csv('ranks.csv')
#scores  = scores.drop('Unnamed: 0', axis =1)
i =0
listd = []
for i in range(1000):
    scores['Customer_id'][i]=1001+i
scores = scores.transpose()

for i in range(50):
    scores.iloc[i+1,1000]=i+101
arr =[]
listd=[]
for i in range(1000):
    scores.sort_values(by=[i],inplace = True)
    arr = scores.iloc[0:10,1000]
    listd.append(arr)
    

merch_recommendations = pd.DataFrame(np.array(listd))
merch_recommendations.to_csv('Merchants_final.csv')
final = pd.read_csv('Merchants_final.csv')

for i in range(1000):
    final['cust_id'][i]=1001+i
    
final.to_csv('Merchants_final.csv')

di = {}
#i =0
for i in range(1000):
    listd.append(di)
    for j in range(50):
        di[j+101] = scores.iloc[i,j]
    
    
    
  
        