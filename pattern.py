#print pattern
print("square pattern")
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()

print("\nupper face triangle")
for a in range(4):
    for b in range(a+1):
        print("#",end="")
    print()   
print("\nlower face triangle")
for m in range(4):
    for n in range(4-m):
        print("#",end="")
    print()   