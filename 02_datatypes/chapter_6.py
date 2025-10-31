chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and bold"
print(f"Firt Word {chai_description[0:8:3]}") #0:8:3 , 3 means skips every third char
print(f"Firt Word {chai_description[:8]}")
print(f"Firt Word {chai_description[5:]}")
print(f"Firt Word {chai_description[::2]}")
print(f"Firt Word {chai_description[::-1]}") # To reverse the string

lable_text = "Chai Special©"
encoded_label = lable_text.encode("utf-8")
print(f"NonEncoded Label : {lable_text}")
decoded_label = encoded_label.decode("utf-8")
print(f"Encoded Label : {decoded_label}")
