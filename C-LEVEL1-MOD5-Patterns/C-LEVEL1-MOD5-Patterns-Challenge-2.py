a=int(input())
if(a%2!=0):
    val=(a-(a%2))/2+1
else:
    val=a//2
    
for i in range(1,a+1):
    for j in range(1,a+1):
        if(a%2 != 0):    
            print("1" if j !=val and i!=val else "0",end="")
        else:
            if(i==val or i==val+1 or j==val+1 or j==val):
                print("0",end="")
            else:
                print("1",end="")
    print()