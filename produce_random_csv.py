# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:56:50 2018

@author: asus
"""

import random

def Y(X1, X2, X3):
 return 0.65 * X1 + 0.70 * X2 - 0.55 * X3 + 1.95

def Produce():
 filename = 'data.csv'
 with open(filename, 'w') as file:
  file.write('0,Y,X1,X2,X3\n')
  for i in range(150):
   random.seed()
   x1 = random.random() * 10
   x2 = random.random() * 10
   x3 = random.random() * 10
   y = Y(x1, x2, x3)
   try:
    file.write(str(i) + ',' + str(y) + ',' + str(x1) + ',' + str(x2) + ',' + str(x3) + '\n')
   except Exception:
    print ('Write Error')
  #  print str(e)
    
if __name__ == '__main__':
 Produce()