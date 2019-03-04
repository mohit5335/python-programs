#prigram for a linear search
pos = -1                                         #position counter
i = 0                                            #index value counter at starting
             
def search(list,n):
    for i in range(len(list)):                   
        if list[i] == n:                    #checking each value through counter
            globals()['pos'] = i            #global keyword pos
            return True
    else:
        return False

def A():
    list = [12,34,65,76,23,98,11,24,54,33]              
    n = int(input("Enter the element you want to search in list : "))   #input from user
    if search(list,n):
        print("Element is found at :",pos)
    else:
        print("Element not found") 

while True:                                             #entering choise to enter program or not
    otp = int(input("\nenter 1 to continue 0 to exit \n"))      
    if(otp==1):
        x = A()
    elif(otp==0):
        break
    else:
        print("Either 1 or 0")   
