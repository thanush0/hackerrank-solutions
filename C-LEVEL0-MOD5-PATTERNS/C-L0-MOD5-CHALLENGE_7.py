a=int(input())*2-1
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==1 or j==1 or i==a or j==a or i==j or i+j==a+1  ):
            print("*",end="")
        else:
            print(" ",end="")
    print()