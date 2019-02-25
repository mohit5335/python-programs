#ways to create array in pyhton
from numpy import *

arr1 = array([1,2,3,4,5])   #array with array function
print("arr1 :",arr1)

arr2 = linspace(1,40,20)   #divides 1 to 40 in 20 equal parts
print("\narr2 :",arr2)

arr3 = logspace(1,40,20)    #divides 1 to 40 in 20 log parts
print("\narr3 :",arr3)

arr4 = arange(1,40,2)       #divides 1 to 40 with gap of 2
print("\narr4 :",arr4)

print("datatype :",(arr1.dtype)) # checks the datatype
print("dimension :",(arr1.ndim))    #checks the dimension of array
print("shape :",(arr1.shape))   #checks the shape (here:(5,1))
print("size :",(arr1.size))     #checks the size (no of elements)

