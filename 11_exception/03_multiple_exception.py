def process_order(item, quantity):
    try:
        if not isinstance(quantity, (int, float)):
            raise TypeError("quantity must be a number")
        price = {"masala" : 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not menu")
    except TypeError as e :
        print(e)

process_order("masala",2)
process_order("masala","two")

# isinstnace to check the type of object or its help to check type of variable too ..
