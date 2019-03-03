#program to take input for an array
import numpy as np
data = list()
num = int(input("Enter the no of elements : "))
for i in range(int(num)):
    n = input("num : ")
    data.append(int(n))
    data.sort()
    a = np.asarray(data)
print(type(a))
print(a[-2])
