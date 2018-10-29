# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:08:56 2018

@author: Harika
"""

#a,b,c =

merch = pd.read_csv('Merchant_details.csv')
merch = merch.iloc[0:50,:]
import pandas as pd
import numpy as np
ranks = [[0 for i in range(50)] for j in range(1000)]
#m = len(merch)
#c = len(custn)

trxn1_pivot = trxn1.pivot_table(index = 'Customer_id', columns = 'Merchant_id', values='Trxn_id', aggfunc='count')
trxn1_pivot = trxn1_pivot.fillna(0)

trxn2_pivot = trxn2.pivot_table(index = 'Customer_id', columns = 'Merchant_id', values='Trxn_id', aggfunc='count')
trxn2_pivot = trxn2_pivot.fillna(0)

trxn3_pivot = trxn3.pivot_table(index = 'Customer_id', columns = 'Merchant_id', values='Trxn_id', aggfunc='count')
trxn3_pivot = trxn3_pivot.fillna(0)

B = [[0 for i in range(3)] for j in range(50)]
"""for i in range(50):
    merch['merchant_id'][i]=i+101
merch.to_csv('Merchant_detals.csv')
"""


B[0][0]=np.mean(trxn1_pivot['101'])

trxn1_pivot = np.array(trxn1_pivot)
trxn2_pivot = np.array(trxn2_pivot)
trxn3_pivot = np.array(trxn3_pivot)

for j in range(50):
    B[j][0]=trxn1_pivot.mean(axis=0)[j]
    B[j][1]=trxn2_pivot.mean(axis=0)[j]
    B[j][2]=trxn3_pivot.mean(axis=0)[j]
    
B = np.array(B)
B = pd.DataFrame(B, columns = ['Cluster1','Cluster2','Cluster3'])

for i in range(50):
    merch['No of transactions'][i]=merch['No of transactions'][i]/1000

B=pd.read_csv('B_values.csv')
A = pd.read_csv('A_mat.csv')
a,b,c = 3.0,2.0,1.0
for i in range(1000):
    id = custn['customer_id'][i]
    if str(id) in clust1['Customer_id'].tolist():
        for j in range(50):
            ranks[i][j] = a*A.iloc[j,i+1]+b*B.iloc[j,1]+c*B.iloc[j,4]
    if str(id) in clust2['Customer_id'].tolist():
        for j in range(50):
            ranks[i][j] = a*A.iloc[j,i+1]+b*B.iloc[j,2]+c*B.iloc[j,4]
    if str(id) in clust3['Customer_id'].tolist():
        for j in range(50):
            ranks[i][j] = a*A.iloc[j,i+1]+b*B.iloc[j,3]+c*B.iloc[j,4]
    
ranks = np.array(ranks)
ranks = pd.DataFrame(ranks, columns = [i for i in range(101,151)])
ranks.to_csv('ranks.csv')
        
        



    
    