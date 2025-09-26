a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        print("1" if i%2 !=0 else "0",end="")
    print()