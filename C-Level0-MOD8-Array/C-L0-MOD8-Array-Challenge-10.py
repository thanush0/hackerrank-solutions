a=int(input())
l=input().split()
count=0
for i in l:
    if i =="0":
        count+=1
print("zc =",count)
print("oc =",a-count)