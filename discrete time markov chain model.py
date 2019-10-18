# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:36:51 2019

@author: gautam
"""
import numpy as np

#data, this can also be imported from a csv
data=[143,152,161,139,137,174,142,141,162,180,164,171,206,193,207,218,229,225,204,200]
data_states=[]
ranges=((100,150), (150,200), (200,250)) #L-M-H
nstates=np.shape(ranges)[0] # shape will return 3x2 and no of states are 3
                            #if no of states were 5, then shape of ranges would have been 5x2

state_values=tuple([x for x in range(1,nstates+1)]) #using it as tuples as no of states wont change
#print(state_values)
#print(nstates)
#print(ranges)

for x in data:
    #print(x)
    for n in range(nstates):
        if x>=ranges[n][0] and x<=ranges[n][1]:
            data_states.append(state_values[n])
            break
print(data_states)

N=np.zeros([nstates,nstates]) #please check for dtype=int as well
'''
data_statess wali list ke consecutive wale elements ki value hi hongi
N wali matrix ke coordinates jo ki increment karne h
Eg: 1 se 2 ho rha h to N12 yani ki N[0][1] increment hoga
ye loop data states ke (second last, last) element tak chalega
therefore loop ki limit is len(data_states)-1
'''
for i in range(0,len(data_states)-1):
    N[data_states[i]-1,data_states[i+1]-1]+=1
#print(N)

P=np.zeros([nstates,nstates])
for i in range(0,nstates):
    for j in range(0,nstates):
        P[i,j]=(N[i,j]/sum(N[i,:]))
print(P)
