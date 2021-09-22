'''
Created on 21-Sep-2021

@author: Rishi
'''
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape)

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print (a) 
b = a.reshape(3,2) 
print(b)

a = np.arange(24) 
print(a)

b = a.reshape(2,4,3) 
print(b)
print (a.itemsize)

a = np.arange(0,24,2) 
print(a)

x = np.linspace(10,20,5, endpoint=False) 
print(x)
