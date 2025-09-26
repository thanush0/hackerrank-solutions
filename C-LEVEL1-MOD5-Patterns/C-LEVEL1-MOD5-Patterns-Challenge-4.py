a=int(input()) 
for i in range(1,a+1):
    for j in range(1,a+1):
        if(a%2!=0):
            print("0" if i==j and a//2+1==i else "1" ,end="")
        else:
            print("0" if  ((a//2==i and i+1==j) or (i==j+1 and a//2==j) or(a//2==i and a//2==j and i==j) or (a//2+1==i and a//2+1==j and i==j) )    else "1" ,end="")
    print()