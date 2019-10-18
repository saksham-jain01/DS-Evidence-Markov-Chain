# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:08:20 2019

@author: gautam
"""

import numpy as np
import pandas as pd


#data, this can also be imported from a csv
data=[143,152,[157,162],139,137,[165,180],142,141,162,180,164,171,[204,209],193,207,[215,220],229,225,204,200]

data_states=[]
ranges=((100,135),(135,165), (165,185),(185,215),(215,250)) #L-LM-M-MH-H #to find the state
ranges_1=((100,150),(135,165), (150,200),(185,215),(200,250)) #To calc the distance

nstates=np.shape(ranges)[0] # shape will return 3x2 and no of states are 3
                            #if no of states were 5, then shape of ranges would have been 5x2

state_values=tuple([x for x in range(1,nstates+1)]) #using it as tuples as no of states wont change

df=pd.read_csv('G:/college/project/markov chain/inventory/BPA_Values.csv', header=None)
m=list(df.values) #matrix to store bpa values 

M=np.zeros([nstates,nstates]) #belief matrix

for i in range(0,nstates):
    for j in range(0,nstates):
        num=0.0
        den=0.0
        for t in range(0,len(data)-1):
            num+=m[t][i]*m[t+1][j]
            den+=m[t][i]
        M[i][j]=num/den


m_new=np.matmul(m[19], M) #m(21)=m(20)*M
m.append(m_new)
#print(m_new)
#print(np.shape(m))

P_low=m[-1][0]+m[-1][1]/2
P_med=m[-1][1]/2+m[-1][2]+m[-1][3]/2
P_high=m[-1][3]/2+m[-1][4]

print([P_low,P_med,P_high])

