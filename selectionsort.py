#program to sort list using selection sort
def sort(list1):
    for i in range(0,len(list1)):
        minpos = i
        for j in range(i,len(list1)):
            if list1[j] < list1[minpos]:
                minpos = j
        temp = list1[i]
        list1[i] = list1[minpos]
        list1[minpos] = temp
    print("List after Sorting",list1)       #list after sorting

list1 = list()                #empty list   
num = int(input("Enter the no of elements : "))     #entering elements of list
for i in range(int(num)):
    n = input("num : ")                             
    list1.append(int(n))

#list1 = [23,56,84,32,65,45,75,12,34,66] (if list is predefined)
print("List before Sorting",list1)          #list after sorting
sort(list1)         #calls sort function
