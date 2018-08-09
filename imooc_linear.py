# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:31:08 2018

@author: asus
"""

import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat

X = mat([1,2,3]).reshape(3,1)
Y = 2*X

#回归拟合
#theta = dot ( dot( inv( dot(X.T,X), X.T), Y)

''' 
梯度下降计算线性回归 
'''
#梯度下降
#theta = theta - alpha*(theta*X -Y)*X
theta = 1.
alpha = 0.1     #(限制下降速率)
for i in range(100):
    theta = theta + np.sum(alpha*(Y- dot(X,theta))*X.reshape(1,3))/3.
    
print(theta)


