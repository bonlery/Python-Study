# ============================================
# WHILE LOOPS
# ============================================

print("=== 1. Basic while loop ===")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

print("\n=== 2. Counter example ===")
count = 10
while count > 0:
    print(count, end=" ")
    count -= 1
print("blast off!")

print("\n=== 3. break - stop the loop early ===")
i = 0
while True:
    print(i, end=" ")
    i += 1
    if i >= 5:
        break
print("- broke out of the loop")

print("\n=== 4. continue - skip this iteration ===")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("- odd numbers only (evens skipped)")

print("\n=== 5. pass - placeholder (does nothing) ===")
i = 0
while i < 3:
    i += 1
    pass                # no-op placeholder
print("loop with pass finished, i =", i)

print("\n=== 6. while True ===")
# Usually needs a break somewhere to avoid an infinite loop
total = 0
i = 1
while True:
    total += i
    i += 1
    if total >= 100:
        break
print("sum until >= 100:", total)

print("\n=== 7. Input-validation loop ===")
# Runs until the user enters a valid answer
answer = ""
while answer.lower() not in ["y", "n"]:
    answer = input("Continue? (y/n): ")
print(f"You answered: {answer}")

print("\n=== 8. else on while (runs when no break) ===")
i = 0
while i < 3:
    print(i, end=" ")
    i += 1
else:
    print("- loop completed without break")
