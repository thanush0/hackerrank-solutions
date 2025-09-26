a , b =map(int,input().split())
c=2
while(True):
    if(c%a==0 and c%b==0):
        break
    else:
        c+=1
print(c)