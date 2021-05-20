# In[1] - Documentation
"""
Script - 02_Numpy_Array.py
Decription - Python NumPy code for array functions
Author - Rana Pratap
Date - 2020
Version - 1.0
"""
print(__doc__)

# In[2] - Import and Creating List Variables
import numpy as np

water_consumption = (200,300,250,167,678)
print(water_consumption)
area =(10,12,9,16,18)
print(area)
water_consumption/area #Error

# In[3] - Creating Array variable
np_water_consumption = np.array(water_consumption) #Array contains one type of data element
type(np_water_consumption)
np_area = np.array(area)
type(np_area)
print(np_water_consumption/np_area)

# In[4] - Creating Array variable - Multitype
var1 = np.array([10.0,'Roger',True])
var1 #Multitype are converted to string type variables

# In[5] - Array addition
age = [18,24,32,56]
age
np_age = np.array(age)
print(np_age)

age1 = age + age
print(age1) # List variables are appended

age2 = np_age + np_age
print(age2) #numpy.ndarray variables are addedy

# In[6] - Subset Array
np_water_consumption
np_water_consumption[1] # Index - 300

np_water_consumption[0:2] # array([200, 300]
np_water_consumption > 250 #Boolean values if the elements are > 250 - array([False,  True, False, False,  True])

np_water_consumption[np_water_consumption > 250] #subset to return element > 250 - array([300, 678])

# In[7] - Two dimensional Array subset
water_consumption
np_water_consumption = np.array(water_consumption)
np_water_consumption #array([200, 300, 250, 167, 678])
area
np_area = np.array(area)
np_area #array([10, 12,  9, 16, 18])

np_ndim = np.array([[200, 300, 250, 167, 678],[10, 12,  9, 16, 18]])
np_ndim
# array([[200, 300, 250, 167, 678],
#[ 10,  12,   9,  16,  18]])

np_ndim.shape #Get the dimensions of the arrary - Rows, Columns - (2, 5)
np_ndim[0] #Get elements of the first row - array([200, 300, 250, 167, 678])
np_ndim[1] #Get elements of the second row - array([10, 12,  9, 16, 18])
np_ndim[0][1] #Get element of first row 2nd element - 300

np_ndim[:,1:3] #Get elements 2nd and 3rd elements of all the rows
#array([[300, 250],
#       [ 12,   9]])
np_ndim[1,:] #Get elements of the second row - array([10, 12,  9, 16, 18])
np_ndim[1,1:4] #Get elements of the second row from 2 to 4 - array([12,  9, 16])

# In[8] - Basic Arthematic
np_ndim.shape #Get Arrary dimensions rows and columns - (2, 5)
np.mean(np_ndim[0]) #Get Mean value - 319.0
np.median(np_ndim[1]) #Get Median value - 12.0
np.corrcoef(np_ndim[0],np_ndim[1]) #Get Correlation Coefficient value
#array([[1.        , 0.62109427],
#       [0.62109427, 1.        ]])
np.std(np_ndim[0]) #Standard Deviation - 185.07728115573775
np.sum(np_ndim[0]) #Sum of rows - 1595
np.sort(np_ndim[1]) #Sorting - array([ 9, 10, 12, 16, 18])

# In[]
del(age,age1,age2,np_age)
del(area,np_area,np_ndim)
del(var1,np_water_consumption,water_consumption)
