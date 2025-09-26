a=int(input())
for n in range(a):
    print("*",end="")
print()
for i in range(a-2):
    print("*",end="")
    for j in range(a-2):
        print(" ",end="")
    for k in range(1):
        print("*",end="")
    print()
for m in range(a):
    print("*",end="")
print()