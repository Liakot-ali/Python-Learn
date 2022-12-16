
import Utils
from Packages import shopping as shop

import random as ran
from pathlib import Path

numbers = [2, 4, 1, 65, 8, -3, 9, 0, 15, 45]

max = Utils.find_max(numbers)
print("Maximum is", max)

min = Utils.find_min(numbers)
print("Minimum is", min)

# Using packages
total = shop.total_amount(numbers)
print("Total amount is :", total)

# Random Value
print("\nRandom")
print(ran.random())
print(ran.randint(20, 58))
print(ran.choice(numbers))

# File
path = Path("")
createPath = Path("./New File")
createPath.rmdir()
print(path.absolute())
for p in path.glob("*.py"):
    print(p)