'''
Created on 21-Sep-2021

@author: Rishi
'''
import numpy as np 
a = np.arange(10) 
print(a)
s = slice(2,7,2) 
print (a[s])
b = a[2:7:2] 
print (b)
print(a[5])
print(a[4:])
print(a[:5])
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print (a[1:])