#program to use anonymous function in python

from functools import reduce                #this is used for reduce function 
 
num = [2,4,6,7,3,5,9,8,1]    #list
#now we will use filter, map and reduce

#suppose we want to find even numbers from list n
"""here comes the comcept of filter"""
even = list(filter(lambda n: n%2 == 0,num))     #it will filter the even numbers from the list  num
print("Even numbers in list num are : ",even)

#suppose we want to double the values of list num
"""here comes the concept of map"""
double = list(map(lambda m: m*2,num))           #it will map the values of list num into list double with dooubling the values
print("Double of list num is : ",double)

#suppose we want to reduce the value of list num to a single value
"""here comes the concept of reduce"""    #lets say want to add all values of num
add = reduce(lambda a,b: a+b,num)
print("Sum of all values of list num is : ",add)
