sugar_amount = 2
print(f"Initial Sugar : {sugar_amount}")

sugar_amount = 15 # we are changing the reference here

print("Initial Sugar : " + str(sugar_amount))
# print("Initial Sugar : {}".format(sugar_amount))

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")