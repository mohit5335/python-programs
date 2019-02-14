# program to addition and multiplication of matrix
            
# First Matrix
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
# Second Matrix
y = [[1,2,3],
     [4,5,6],
     [7,8,9]] 
 #Resultant Matrix   
add = [[0,0,0],
     [0,0,0],
     [0,0,0]]

multi = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        add[i][j] = x[i][j] + y[i][j]
        multi[i][j] = x[i][j] * y[i][j]
print("Addition of x and y\n")
for r in add:
    print(r)
print("Multiplication of x and y\n")
for s in multi:
    print(s)

