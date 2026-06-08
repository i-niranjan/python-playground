class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()

print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup ="small"

print("After Changing", cutting.temperature)
print("Cup Size is", cutting.cup)
print("Direct Look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
# print(cutting.cup) Attribute error if del is done.