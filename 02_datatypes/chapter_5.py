

from decimal import Decimal

ideal_temp = Decimal("95.5")
current_temp = Decimal("95.499999999999")

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Diff temp { ideal_temp - current_temp}")

