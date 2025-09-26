a=int(input())
b=sorted(input().split())
dupli=[x for x in b if b.count(x)>1]
c=0
for i in dupli:
    if b.count(i)>a//2:
        print(f"The majority element is : {i}")
        break
    else:
        c=1
else:
    if c==1:        
        print("No majority element found in the array")