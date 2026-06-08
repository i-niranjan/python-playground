class Chai:
    origin = "India"

print(Chai.origin)


Chai.is_hot = True
print(Chai.is_hot)

# creating object from class Chai

masala = Chai()

print(f"Masala {masala.is_hot}")
print(f"Masala {masala.origin}")
masala.is_hot = False

print("Class: ")

masala.flavor = "Masala"
print(masala.flavor)
