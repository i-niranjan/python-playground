# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams

print(f"Total Grams : {total_grams}")

milt_litres = 7
servings = 4

milk_per_serving = milt_litres/servings

print(f"Milk per servings is : {milk_per_serving}")

total_tea_bags = 7
pots = 4

bags_per_pot = total_tea_bags // pots  #fogot about decimals
print(f"Tea bas per pot : {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup #Remainder
print(f"Left Over Pods : {leftover_pods}")

base_falvour_strength = 2
scale_factor = 3
powerful_flavour = base_falvour_strength ** scale_factor # exponentital 2 to the power of 3
print(f"Scaled Flavour strenght is {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000  #just to improve the readabilty
print(f"Tea Leaves : ${total_tea_leaves_harvested}")