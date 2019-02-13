# program to find hcf and lcm of the given numbers
"""enter number from users"""

print("Program to find HCF and LCM of the given numbers")

# HCF or GCD
def hcf(x,y):
    #choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if((x % i == 0 ) and (y % i == 0)):
            hcf = i
    return hcf
#LCM    
def lcm(x,y):
    lcm = (x*y) // hcf(x,y)         # we know [number1 * number2] = [LCM * HCF]
    return lcm
              
while(True):
    otp = int(input("\nenter 1 to continue 0 to exit\n"))      #want to check for more 
    if(otp==1):
        a = int(input("Enter 1st number : "))               #enter input from user
        b = int(input("Enter 2nd number : "))
        print("HCF of",a,"and",b,"= : ",hcf(a,b))           #calling hcf
        print("\nLCM of",a,"and",b,"= : ",lcm(a,b))         #calling lcm
    elif(otp==0):
        break
    else:
        print("Either 0 or 1")
    
