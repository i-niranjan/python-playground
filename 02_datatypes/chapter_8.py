# Lists

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maxium sugar level : {max(sugar_levels)}")
print(f"Minimum sugar level : {min(sugar_levels)}")

# Operator Overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black_tea"] * 3
print(f"Strong brew : {strong_brew}")

# Byte Array

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data =  raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw Spice Data : {raw_spice_data}")
