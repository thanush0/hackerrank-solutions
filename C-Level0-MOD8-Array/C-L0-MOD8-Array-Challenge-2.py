a=int(input())
b=input().split()
even=0
for i in b:
    if int(i)%2==0:
        even+=1
print("Odd =",a-even )
print("Even =",even)