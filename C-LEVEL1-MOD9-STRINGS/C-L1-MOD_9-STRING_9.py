a=input()
flag=1
for i in range(len(a)):
    if a[0]==")":
        flag+=1
        break
    if a[i]=="(":
        flag+=1
    elif a[i]==")":
        flag-=1
    '''print(flag)'''
if flag ==1:
    print("Balanced")
else:
    print("Unbalanced")