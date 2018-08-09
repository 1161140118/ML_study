# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:52:48 2018

@author: asus
"""

import numpy as np
from numpy.linalg import inv
from numpy import dot,mat
import pandas as pd

dataset = pd.read_csv('data.csv')
#print(dataset)

temp = dataset.iloc[:,2:5]   
temp['x0'] = 1  # bias

X = temp.iloc[:,[3,0,1,2]]  
#print(X)

Y = dataset.iloc[:,1]
#print(len(Y))

#最小二乘法
theta = dot( dot( inv( dot(X.T, X)), X.T) ,Y)
print(theta)

#梯度下降
theta = np.array([1.,1.,1.,1.]).reshape(4,1)
alpha = 0.1 
temp = theta
Y = Y.values.reshape(len(Y),1)
length = float( len(Y))


X0 = X.iloc[:,0].values.reshape(len(Y),1)
X1 = X.iloc[:,1].values.reshape(len(Y),1)
X2 = X.iloc[:,2].values.reshape(len(Y),1)
X3 = X.iloc[:,3].values.reshape(len(Y),1)


for i in range(50):
    temp[0] = theta[0] + alpha*(np.sum( (Y-dot(X, theta))*X0 ))/length
    temp[1] = theta[1] + alpha*(np.sum( (Y-dot(X, theta))*X1 ))/length
    temp[2] = theta[2] + alpha*(np.sum( (Y-dot(X, theta))*X2 ))/length
    temp[3] = theta[3] + alpha*(np.sum( (Y-dot(X, theta))*X3 ))/length
    theta = temp
    
print(theta)

