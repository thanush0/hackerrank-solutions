a=int(input())
i=0
for j in range(1,a):
    if(a%j==0):
        i+=j
if(i==a):
    print("Perfect Number")
elif(i>a):
    print("Abundant Number")
else:
    print("Deficient Number")