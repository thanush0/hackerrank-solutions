a=int(input())
b=input().split()
print(int(b[0])*int(b[1]),end=" ")
for i in range(1,a-1):
        print(int(b[i+1])*int(b[i-1]),end=" ")
print(int(b[a-2])*int(b[a-1]),end=" ")