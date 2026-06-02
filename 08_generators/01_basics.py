import time

# ============================================================
# SECTION 1: Normal function vs Generator — Memory difference
# ============================================================

def get_chai_list():
    print("  [list] Building ALL cups at once...")
    return ["Cup 1: Masala", "Cup 2: Ginger", "Cup 3: Elaichi"]

def get_chai_gen():
    print("  [gen] Making Cup 1...")
    yield "Cup 1: Masala"

    print("  [gen] Making Cup 2...")
    yield "Cup 2: Ginger"

    print("  [gen] Making Cup 3...")
    yield "Cup 3: Elaichi"

    print("  [gen] Stall closed. No more chai.")


print("=" * 50)
print("SECTION 1: When does execution happen?")
print("=" * 50)

print("\n-- Normal function --")
print("Calling get_chai_list()...")
chai_list = get_chai_list()           # runs FULLY right here
print("Got:", chai_list)

print("\n-- Generator function --")
print("Calling get_chai_gen()...")
chai_gen = get_chai_gen()             # does NOT run yet! just creates generator
print("Got:", chai_gen)               # <generator object> — nothing made yet

print("\nNow calling next()...")
cup = next(chai_gen)                  # runs until first yield, then PAUSES
print("Received:", cup)

print("\nCalling next() again...")
cup = next(chai_gen)                  # resumes from after first yield
print("Received:", cup)

print("\nCalling next() again...")
cup = next(chai_gen)
print("Received:", cup)

# next() on exhausted generator raises StopIteration
print("\nCalling next() one more time (generator is exhausted)...")
try:
    next(chai_gen)
except StopIteration:
    print("  StopIteration raised — generator is done!")


# ============================================================
# SECTION 2: for loop does next() automatically
# ============================================================

print("\n" + "=" * 50)
print("SECTION 2: for loop = automatic next() calls")
print("=" * 50)

print("\nLooping over a fresh generator:")
for cup in get_chai_gen():
    print("  Serving:", cup)
    time.sleep(0.3)   # feel the one-at-a-time delivery


# ============================================================
# SECTION 3: Memory — generator vs list for large data
# ============================================================

print("\n" + "=" * 50)
print("SECTION 3: Memory — list vs generator at scale")
print("=" * 50)

def big_list(n):
    return [i * i for i in range(n)]     # builds ALL n numbers in RAM

def big_gen(n):
    for i in range(n):
        yield i * i                       # produces ONE number at a time

import sys

n = 100_000
lst = big_list(n)
gen = big_gen(n)

print(f"\nList      of {n} items : {sys.getsizeof(lst):,} bytes in memory")
print(f"Generator of {n} items : {sys.getsizeof(gen):,} bytes in memory")
print("Generator size stays constant no matter how large n gets!\n")


# ============================================================
# SECTION 4: Generator with send() — two-way communication
# ============================================================

print("=" * 50)
print("SECTION 4: Generator state — it remembers where it paused")
print("=" * 50)

def running_total():
    total = 0
    while True:
        amount = yield total     # pause here, send back total, wait for next value
        total += amount

wallet = running_total()
next(wallet)                     # prime the generator (reach first yield)

print("\nAdding money to wallet:")
print("  After +100 :", wallet.send(100))
print("  After +250 :", wallet.send(250))
print("  After +50  :", wallet.send(50))
# Generator remembers 'total' across every send — no global variable needed
