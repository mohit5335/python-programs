#initailize array
a = [4,7,2,8,9,2,3,1]
temp = 0

#Original Array
print("Elements of Original array : ")
for i in range (0,len(a)):
    print(a[i])
    
#Sort array in decending order
for i in range(0, len(a)):    
    for j in range(i+1, len(a)):    
        if(a[i] < a[j]):    
            temp = a[i];    
            a[i] = a[j];    
            a[j] = temp;    
     

#Displaying elements of array after sorting    
print("Elements of array sorted in descending order: ")    
for i in range(0, len(a)):     
    print(a[i]),   