a=int(input())
b=input().split()
sum=0
for i in range(a):
    sum+=int(b[i])
for i in range(a):
    print(sum-int(b[i]),end=" ")