def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


refill = infinite_chai()


for ___ in range(3):
    print