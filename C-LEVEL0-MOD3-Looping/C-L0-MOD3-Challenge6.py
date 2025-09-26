a , b =map(int,input().split())
flag=0
while(a>=b):
    a-=b
    flag+=1
print(flag)