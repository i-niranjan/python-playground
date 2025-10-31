# Boolean

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions : {total_actions}")

milk_present = 0
print(f"Is there milk ? {bool(milk_present)}") #bool will convert 0,None,'',[],{},False,set() to false everything else to true

#Logical Operations - and or not

water_hot = True
tea_added = True

can_server = water_hot and tea_added

print(f"Can we server : {can_server}")