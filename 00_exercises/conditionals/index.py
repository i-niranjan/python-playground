number = int(input("Please enter number : "))

if number == 0:
    print("Its zero")
elif number % 2 == 0:
    print(f"Number {number} is Even")
else:
    print(f"Number {number} is Odd")

if number > 0:
    print("Its positive")
elif number <0:
    print("Its negative")

if number >= 18:
    print("Eligible to vote")
elif number <18 and number > 0:
    print("Not Eligible to vote")