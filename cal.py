# Program make a simple calculator that can add, subtract, multiply and divide using functions#

#this function adds two numbers
def add(x,y):
    return (x+y)
#this function subtracts two numbers
def subtract(x,y):
    return(x-y)
#this function multiplies two numbers
def multiply(x,y):
    return(x*y)
#this function divides two numbers
def divide(x,y):
    return(x/y)
#this function gives x to the power y
def power(x,y):
    return(x**y)    
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

#take input from user
n1 = int(input("Enter first number : "))
n2 = int(input("Enter Second number : "))

#enter choice from user
choice=input("Enter Choice 1/2/3/4/5 : ")
if choice == '1':
    print( n1, "+", n2, "=",add(n1,n2) )
elif choice == '2':
    print( n1, "-", n2, "=",subtract(n1,n2) )
elif choice == '3':
    print( n1, "*", n2, "=",multiply(n1,n2) )
elif choice == '4':
    print( n1, "/", n2, "=",divide(n1,n2) )
elif choice == '5':
    print( n1, "^", n2, "=",power(n1,n2) ) 
else:
    print("Invalid Choice")
    print("Please choose from 1 to 5")