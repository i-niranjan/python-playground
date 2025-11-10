seat_type =  input("Enter seart type (sleeper/AC/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC , Beds Available")
    case "ac":
        print("AC - Air Condtioned")
    case "general":
        print("Cheapest Opt.")
    case "luxury":
        print("Wohooo")
    case _:
        print("Invalid Seat type")
