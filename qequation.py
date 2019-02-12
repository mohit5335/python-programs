#program to find the roots of a quadratic equation
# ax**2 + bx + c = 0
# import complex module
import cmath
# take value of a,b and c from user
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

# calculating discriminant
d = (b**2) - (4*a*c)
# finding the square root of d
D = cmath.sqrt(d)
#finding the roots 
x1 = (- b - D) / (2*a)
x2 = (- b + D) / (2*a)
print("The roots of the equation are\n",x1,"\n",x2)