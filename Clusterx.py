# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:51:55 2018

@author: Harika
"""
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import seaborn as sns
import random

import pandas as pd
cust = pd.read_csv('Customer_details.csv');
import numpy as np
X = cust.iloc[:,0:10].values

cust = cust.drop('Unnamed: 10', axis =1)
cust = cust.drop('Unnamed: 11', axis =1)
cust = cust.drop('Unnamed: 12', axis =1)

cust_copy = cust.copy()
k = len(cust)
i =0
for i in range(k):
    if(cust['age'][i]<20 and cust['income'][i]>50000):
        cust['income'][i] = random.randint(4000,25000) 
    if(cust['age'][i]>70 and cust['income'][i]>70000):
        cust['income'][i] = random.randint(30000,65000)
        
cust.to_csv('customer_details.csv', encoding='utf-8', index=False)        

cust[1,:]#kmeans = KMeans(n_clusters=4)
cust.index[2]
#k = 4

da = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
p = da[0]

#km = KMeans()









cust_np = cust.as_matrix()

km = KMeans(n_clusters = 2)
km.fit(cust_np[:,2:5])
y_kmeans = km.predict(cust_np[:,2:5])

plt.scatter(cust_np[:, 2], cust_np[:, 3], c=y_kmeans, cmap='viridis')


plt.scatter(cust_np[:, 2], cust_np[:, 3])

cust_np[:,2:3]
cust[2]

type(cust['income'][1])