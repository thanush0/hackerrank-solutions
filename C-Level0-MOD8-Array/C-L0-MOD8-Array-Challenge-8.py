a=int(input())
b=input().split()
for j in range(1,a):
    sum=0
    for i in range(j,a):
        sum+=int(b[i])
    print(sum,end=" ")
print("0")