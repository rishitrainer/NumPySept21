'''
Created on 21-Sep-2021

@author: Rishi
'''
import numpy as np 
dt = np.dtype(np.int32) 
print(dt)
dt = np.dtype('i4')
print(dt)
dt = np.dtype([('age',np.float32)])
a = np.array([(10,),(20,),(30,)], dtype = dt)  
print(a)

# Complex 
student_dt = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('David', 21, 50),('Brian', 18, 75)], dtype = student_dt) 
print(a)