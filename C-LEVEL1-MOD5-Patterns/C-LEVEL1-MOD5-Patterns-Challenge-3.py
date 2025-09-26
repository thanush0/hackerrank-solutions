a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        print("1" if i==a or j==a or i==1 or j==1 else "0",end="")
    print()