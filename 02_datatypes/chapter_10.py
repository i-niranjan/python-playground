chai_order = dict(type = "Masala Chai" ,  size = "Large" , sugar = 2)
# print(f"Chai Order : {chai_order}")

chai_recipe  =  {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai Recipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"Chai Recipe : {chai_recipe}")

# Memebership test
print(f"Is sugar is in order ? {'sugar' in chai_order}")
chai_order ={"type" : "Masala Chai" ,  "size" : "Large" , "sugar" : 2}

print(f"Order details (keys) : {chai_order.keys()}")
print(f"Order details (values) : {chai_order.values()}")
print(f"Order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"removed item : {last_item}")

extra_spices = {"cardamom" : "crushed" , "ginger" : "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated Chai Recipe : {chai_recipe}")

customer_note = chai_order.get("note", "No Note") #To provide a default value
print(f"Chai size is : {customer_note}")