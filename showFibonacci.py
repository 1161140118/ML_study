# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:36:51 2018

@author: asus
"""
import matplotlib.pyplot as plt

a= [1,1]
b= []
c= []

for i in range(100):
    a += [a[i]+a[i+1]]
    b += [a[i]/a[i+1]]
    c += [i]
    

plt.plot(c[10:],b[10:])
plt.show()
print(b[-1])