#take input from user
data = input("Enter your password\n")
f1 = 0 
f2 = 0 
f3 = 0 
f4 = 0
l = len(data)
#checking length of password
if(l >= 8):
    f1 = True
#checking for upper case and lower case
if(data.upper() != data and data.lower() != data):
    f2 = True
#checking presence of special characters
for var in range(l):
    f3 = not(data[var].isalpha()) and not(data[var].isnumeric())
    if(f3 == True):
        break
#checking for numerics
for var in range(l):
    f4 = data[var].isnumeric()
    if(f4 == True):
        break
#for all above conditions 
if(f1 and f2 and f3 and f4):
    print("Password is valid")
else:
    print("Password is not valid")