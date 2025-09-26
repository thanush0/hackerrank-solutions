a=input()
if a.islower():
    if ".com" in a :
        if "@" in a:
            if "gmail" or "yahool" in a:
                print("Valid")
            else:    
                print("Invalid")
        else:    
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")