a=int(input())
b=input().split()
c=[]
for i in range(a):
    c.append(int(b[i]))
if len(b)==a:
    print(min(c))