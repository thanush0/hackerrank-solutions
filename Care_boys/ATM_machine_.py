amount = int(input())

print("Total number of notes:")

notes = [500, 100, 50, 20, 10, 5, 2, 1]
store = amount

for note in notes:
    count = store // note
    print(f"{note} : {count}")
    store = store % note