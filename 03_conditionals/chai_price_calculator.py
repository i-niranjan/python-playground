cup = input("Choose your cup size (small/medium/larger): ").lower()

if cup == "small":
    print("Price is 10 rs.")
elif cup == "medium":
    print("Price is 15 rs.")
elif cup == "large":
    print("Price is 20 rs.")
else:
    print("Invalid Cup Size")