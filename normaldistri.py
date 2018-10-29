# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:19:12 2018

@author: Harika
"""

from scipy.stats import truncnorm

from scipy import stats
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd

custn = pd.read_csv('customer_new1.csv');
import numpy as np


custn = custn.drop('Unnamed: 10', axis =1)
custn = custn.drop('Unnamed: 11', axis =1)
custn = custn.drop('Unnamed: 12', axis =1)
arr = list(range(1000))

#custndup = custn.copy()
k = len(custndup)
i =0
for i in range(k):
    if(custndup['age'][i]<30 and custndup['income'][i]>50000):
        custndup['income'][i] = random.randint(4000,80000) 
    if(custndup['age'][i]>65 and custndup['income'][i]>70000):
        custndup['income'][i] = random.randint(30000,65000)
    

#custndup = custn.copy()




plt.scatter(arr,ran)
plt.scatter(custn_np[:, 2], custn_np[:, 3])

plt.xlabel('age')
plt.ylabel('income')

trxn['Trxn_id'].nunique()



def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
  
    
tr = get_truncated_normal(mean=5000, sd = 10000, low = 10, upp = 10000)
trn = tr.rvs(len(trxn))
    
ra = get_truncated_normal(mean=45, sd=10, low=17, upp=80)
ran = ra.rvs(1000)

for i in range(1000):
    custndup['age'][i]=int(round(ran[i]))
    custndup['income'][i] = int(round(rain[i]))

for i in range(len(trxn)):
    trxn['Price'][i]=int(round(trn[i]))
    
trxn.to_csv('trxn_details_new.csv')
#custndup = custn.copy()    
custndup['age'] = ran

rai = get_truncated_normal(mean=80000,sd = 30000, low = 8000, upp = 150000)
rain = rai.rvs(1000) 
custndup['income'] = rain  

from scipy.spatial.distance import cdist
distortions = []
K = range(1,10)
D = custn_np[:,2:9]
for k in K:
    km = KMeans(n_clusters=k).fit(D)
    km.fit(D)
    distortions.append(sum(np.min(cdist(D, km.cluster_centers_, 'euclidean'), axis=1)) / D.shape[0])
    
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()


custn_np = custndup.as_matrix()
km = KMeans(n_clusters = 3)
km.fit(custn_np[:,2:9])
y_kmeans = km.predict(custn_np[:,2:9])
from mpl_toolkits.mplot3d import axes3d
X = custn_np[:,2]
Y = custn_np[:,3]
Z = custn_np[:,4]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('$Age$')
ax.set_zlabel('$Income$')
ax.set_ylabel('$No of trxns$')
ax.scatter(X,Z,Y, c=y_kmeans, cmap="RdBu")
plt.show()
    

plt.scatter(custna[:, 2], custna[:, 3])

custndup['cluster']=y_kmeans
for i in range(1000):
    custndup['customer_id'][i]=i+1001
    
merch.to_csv('Merchant_details.csv')
#custndup.to_csv('customer_new1.csv', encoding='utf-8', index=False)       
    
    
    