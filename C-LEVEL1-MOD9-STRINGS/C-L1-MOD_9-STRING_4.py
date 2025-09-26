a=sorted(input())
flag=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print("NOT ISOGRAM")
        flag=0
        break
    else:
        flag=1
        
if flag==1:
    print("ISOGRAM")