# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:34:11 2019

@author: gautam
"""

import numpy as np
import pandas as pd

def distance_calc(a1,a2,b1,b2):
    ans=((a1+a2)/2-(b1+b2)/2)**2 +(1/12)*((a2-a1)-(b2-b1))**2
    ans=ans**0.5
    return ans


#data, this can also be imported from a csv
data=[143,152,[157,162],139,137,[165,180],142,141,162,180,164,171,[204,209],193,207,[215,220],229,225,204,200]

data_states=[]
ranges=((100,135),(135,165), (165,185),(185,215),(215,250)) #L-LM-M-MH-H #to find the state
ranges_1=((100,150),(135,165), (150,200),(185,215),(200,250)) #To calc the distance

nstates=np.shape(ranges)[0] # shape will return 3x2 and no of states are 3
                            #if no of states were 5, then shape of ranges would have been 5x2

state_values=tuple([x for x in range(1,nstates+1)]) #using it as tuples as no of states wont change
#print(state_values)
#print(nstates)
#print(ranges)
distance=np.zeros([len(data), nstates])
t=0
for x in data:
    if type(x) is not int:
        a1,a2=x[0],x[1]
        x=x[0]
    else:
        a1,a2=x,x
    
    for n in range(nstates):
        if x>=ranges[n][0] and x<=ranges[n][1]:
            data_states.append(state_values[n])
            break
        
    for i in range(nstates):
        b1=ranges_1[i][0]
        b2=ranges_1[i][1]
        distance[t][i]=distance_calc(a1,a2,b1,b2)
    t+=1
print(data_states)
print(distance)


df = pd.DataFrame(distance)
df.columns=["D1", "D2","D3","D4","D5"]
df.set_index(np.array([x for x in range(1,len(data)+1)]))
print(df)
#df.to_csv("G:/college/project/markov chain/inventory/distance.csv")


'''
N=np.zeros([nstates,nstates]) #please check for dtype=int as well

data_statess wali list ke consecutive wale elements ki value hi hongi
N wali matrix ke coordinates jo ki increment karne h
Eg: 1 se 2 ho rha h to N12 yani ki N[0][1] increment hoga
ye loop data states ke (second last, last) element tak chalega
therefore loop ki limit is len(data_states)-1

for i in range(0,len(data_states)-1):
    N[data_states[i]-1,data_states[i+1]-1]+=1
#print(N)

P=np.zeros([nstates,nstates])
for i in range(0,nstates):
    for j in range(0,nstates):
        P[i,j]=(N[i,j]/sum(N[i,:]))
print(P)
'''