a=int(input())
for i in range(1,a+1):
    value=1
    for j in range(1,i+1):
        if i%2==0:
            print(value*2,end="")
            value+=1
        else:
            print(value,end="")
            value +=2
    print()