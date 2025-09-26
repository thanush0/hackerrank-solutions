a=input().replace(" ","")
b=input().replace(" ","")
if(sorted(a)==sorted(b)):
    print(f"{a} and {b} are Anagrams.")
else:
    print(f"{a} and {b} are Not Anagrams.")