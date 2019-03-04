#program to implement binary search
pos = -1                    #positional counter

def search(list1,n):
    l = 0
    u = len(list1)-1
    while l <= u:
        mid = (u + l)//2
        if list1[mid] == n:                  # ie; if mid vlaue == the value we are searching
            globals()['pos'] = mid          #global keyword pos
            return True
        else:
            if list1[mid] < n:
                l = mid + 1                 #redefining value of l
            else:
                u = mid - 1                 #redefining value of u
    return False            

def A():
    list1 = [12,34,65,76,23,98,11,24,54,33]  
    list1.sort()                                   #sorting the list as binary search works in sorted list
    n = int(input("Enter the element you want to search in list : "))   #input from user
    if search(list1,n):
        print("Element is found at index :",pos)
    else:
        print("Element not found") 
while True:                                             #entering choise to enter program or not
    otp = int(input("\nenter 1 to continue 0 to exit \n"))      
    if(otp==1):
        A()
    elif(otp==0):
        break
    else:
        print("Either 1 or 0")   
