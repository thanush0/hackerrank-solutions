a=int(input())
flag=0
for i in range(1,a+1):
    if(a==2**i):
        flag+=1
if(flag==1):
    print("YES")
else:
    print("NO")