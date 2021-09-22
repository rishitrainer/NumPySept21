'''
Created on 21-Sep-2021

@author: Rishi
'''
import numpy as np

# Arrays - N Dimentional - 3 

a = np.array([1,2,3,4,5,6,7], ndmin = 2) 
print(a)

a = np.array([[1, 2], [3, 4]]) 
print(a)

a = np.array([[[1, 2], [3, 4]], [[5,6], [7,8]]]) 
print(a)

a = np.array([1,2,3,4,5,6,7], dtype=complex) 
print(a)