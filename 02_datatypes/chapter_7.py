# tuples

masala_spices = ("carrdamom","cloves","cinnamon")
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices : {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio for ginger {ginger_ratio} and C is {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio # swap
print(f"Ratio for ginger {ginger_ratio} and C is {cadramom_ratio}")

# membership

print(f"Is ginger is in masala spices ? => {'ginger' in masala_spices}")
print(f"Is cinnamon is in masala spices ? => {'cinnamon' in masala_spices}")