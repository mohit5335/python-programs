#python program to show recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1) 

print("Program to find the Factorial of the number using recursion")
while(True):
    otp = int(input("\nenter 1 to continue 0 to exit \n"))      #want to check for more 
    if(otp==1):
        x = int(input("\nEnter the Number : "))        
        result = fact(x) 
        print("\nFactorial of {} is".format(x),result)
    elif(otp==0):
        break
    else:
        print("Either 1 or 0")
        
      


