name= ["hitesh","meera","sam","ali"]
bills = [50,70,100,55]

for item, item2 in zip(name, bills):
    print(f"{item} paid {item2} rs")