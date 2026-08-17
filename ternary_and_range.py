# ============================================
# TERNARY + SHORTHAND FOR LOOP + RANGE
# ============================================

print("=== 1. Ternary (shorthand if/else) ===")
# Syntax: <value if true> if <condition> else <value if false>
age = 20
status = "adult" if age >= 18 else "minor"
print("age 20 ->", status)

x = 5
result = "even" if x % 2 == 0 else "odd"
print("5 is", result)

print("\n=== 2. end=' ' keeps output on one line ===")
for i in range(5):
    print(i, end=" ")
print()                              # newline at the end

print("\n=== 3. range(10)  -> stop -> 0,1,2,3,4,5,6,7,8,9 ===")
print(list(range(10)))

print("\n=== 4. range(1, 10)  -> start=1, stop=10 -> 1 to 9 ===")
print(list(range(1, 10)))

print("\n=== 5. range(1, 10, 2)  -> start, stop, step ===")
print(list(range(1, 10, 2)))

print("\n=== 6. for i in range(10, 0, 2) ===")
for i in range(10, 0, 2):
    print(i)
# -> walang nangyayari, walang output, walang ring error
#    because start (10) > stop (0) but step is positive
print("(no output above: positive step can't reach 0 from 10)")

print("\n=== 7. range with a negative step (actually works) ===")
for i in range(10, 0, -2):
    print(i, end=" ")
print()

print("\n=== 8. Shorthand loop with comprehension (see list_comprehensions.py) ===")
print([i * i for i in range(1, 6)])  # squares of 1..5
