# In[1] - Documentation
"""
Script - #01_NumPy_Input-Output.py
Decription - Code to read and write text file using Python NumPy from 
https://numpy.org/
https://numpy.org/doc/stable/

Author - Rana Pratap
Date - June 2021
Version - 1.0
"""
print(__doc__)
print(np.__version__)

# In[2] - Import and Read Data as an Array
import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print('-'*40)

b = np.arange(10).reshape(-1, 1)
print(b)
print('-'*40)

c = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
print(c)
print('-'*40)

# In[3] - Read and Write files as .npy
np.save('outfile',a)
print('File saved as *.npy')

b = np.load('outfile.npy')
print('Data loaded from *.npy')
print(b)
print('-'*40)

# In[4] - Read and Write files as .txt
np.savetxt('outfile.txt',a)
print('File saved as *.txt')

c = np.loadtxt('outfile.txt')
print('Data loaded from *.txt')
print(c)
print('-'*40)
##======================================================================================
del(a,b,c)

