a=input()
flag=0
for i in a :
    if i.isdigit():
        print(i,end="")
    else:
        flag=flag+1
if flag==len(a):
    print("0")