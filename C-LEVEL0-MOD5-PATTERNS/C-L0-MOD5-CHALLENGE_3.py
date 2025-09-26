a=int(input())
count=1
for i in range(1,a+1):
    for j in range(1,a+1):
        print(int(not(i+j)%2),end="")
    print()