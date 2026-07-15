"""
Generators - Drills

Goal: understand how yield pauses and resumes function execution.
"""

# Drill 1:
# Write a simple generator that yields "start", "middle", "end".
# Use next() to read each value.


# Drill 2:
# Write a generator that yields numbers 1, 2, 3.
# Loop through it with a for loop.


# Drill 3:
# Convert this list-returning function into a generator.
def get_squares(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


# Drill 4:
# Write a generator that yields characters from a string one by one.


# Drill 5:
# Write a generator that yields only active users.
users = [
    {"name": "Niranjan", "active": True},
    {"name": "Amit", "active": False},
    {"name": "Sara", "active": True},
]

