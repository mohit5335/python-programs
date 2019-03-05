#program to sort list using bubble sort
def sort(list1):
    for i in range(len(list1)-1,0,-1):      #outer loop from length of list to first index
        for j in range(i):                  #inner loop for checking each element
            if list1[j] > list1[j+1]:
                temp = list1[j]             #temporary variable for holding first value
                list1[j] = list1[j+1]       
                list1[j+1] = temp
    print("List after Sorting",list1)       #list after sorting

list1 = list()                #empty list   
num = int(input("Enter the no of elements : "))     #entering elements of list
for i in range(int(num)):
    n = input("num : ")                             
    list1.append(int(n))

#list1 = [23,56,84,32,65,45,75,12,34,66] (if list is predefined)
print("List before Sorting",list1)          #list after sorting
sort(list1)         #calls sort function
