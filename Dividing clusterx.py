# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:13:17 2018

@author: Harika
"""




import pandas as pd

custn = pd.read_csv('customer_new1.csv');
import numpy as np
# dividing into different xls
custna = custn.iloc[:,:].values

k = len(custn)
clust1 = []
clust2 = []
clust3 = []

c=0
for i in custna:
    if(i[10]==0):
        clust1.append(i.tolist())
    if(i[10]==1):
        clust2.append(i.tolist())
    elif(i[10]==2):
        clust3.append(i.tolist())
        
        
        #print(c)
    #c+=1
        
clust1 = np.array(clust1)
clust1 = pd.DataFrame(clust1, columns = ['profession', 'Customer_id','Age','income','No of transactions','Home_latitude','Home_longitude','work_long','work_lat','Gender','cluster'])
       
clust2 = np.array(clust2)
clust2 = pd.DataFrame(clust2, columns = ['profession', 'Customer_id','Age','income','No of transactions','Home_latitude','Home_longitude','work_long','work_lat','Gender','cluster'])
       
clust3 = np.array(clust3)
clust3 = pd.DataFrame(clust3, columns = ['profession', 'Customer_id','Age','income','No of transactions','Home_latitude','Home_longitude','work_long','work_lat','Gender','cluster'])
        
clust1.to_csv('cust_cluster1.csv')
clust2.to_csv('cust_cluster2.csv')
clust3.to_csv('cust_cluster3.csv')

trxn=pd.read_csv('trxn_details_new.csv')
#trxn.drop('Index', axis=1)


trxn1 = []
trxn2 = []
trxn3 = []
k = len(trxn)
Xt = trxn.iloc[:,:].values
#trxn = trxn.drop('Unnamed: 0',axis=1)
for i in Xt:
    if str(i[2]) in clust1['Customer_id'].tolist():
        trxn1.append(i.tolist())
    elif str(i[2]) in clust2['Customer_id'].tolist():
        trxn2.append(i.tolist())
    elif str(i[2]) in clust3['Customer_id'].tolist():
        trxn3.append(i.tolist())
    else:
        print(i[2])
        

trxn1 = np.array(trxn1)
trxn2 = np.array(trxn2)
trxn3 = np.array(trxn3)

trxn1 = pd.DataFrame(trxn1, columns = ['Trxn_date', 'Trxn_id','Customer_id','Merchant_id','Price'])
trxn2 = pd.DataFrame(trxn2, columns = ['Trxn_date', 'Trxn_id','Customer_id','Merchant_id','Price'])
trxn3 = pd.DataFrame(trxn3, columns = ['Trxn_date', 'Trxn_id','Customer_id','Merchant_id','Price'])



