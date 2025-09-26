a=(input().replace(" ","")).lower()
b=sorted(set(ch for ch in a if ch.isalpha()))
print("Pangrams" if len(b)==26 else "Not Pangrams")