# ============================================
# CONDITIONALS
# ============================================

print("=== 1. if / elif / else ===")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

print("\n=== 2. Nested conditionals ===")
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Allowed in")
    else:
        print("Need an ID")
else:
    print("Too young")

print("\n=== 3. Comparison operators ===")
print("== :", 5 == 5)
print("!= :", 5 != 3)
print("<  :", 3 < 5)
print(">  :", 5 > 3)
print("<= :", 5 <= 5)
print(">= :", 5 >= 6)

print("\n=== 4. Logical operators ===")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)
a, b = 5, 10
print("(a > 0) and (b < 20):", (a > 0) and (b < 20))
print("(a > 10) or (b > 5):", (a > 10) or (b > 5))

print("\n=== 5. Membership operators ===")
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", "banana" in fruits)
print("'grape' in fruits:", "grape" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)
print("'h' in 'hello':", "h" in "hello")
print("3 in {1, 2, 3}:", 3 in {1, 2, 3})

print("\n=== 6. Identity operators ===")
x = [1, 2]
y = x            # same object
z = [1, 2]       # different object, same value
print("x is y:", x is y)          # True  (same object)
print("x is z:", x is z)          # False (different objects)
print("x is not z:", x is not z)  # True
print("x == z:", x == z)          # True  (equal value)

print("\n=== 7. Truthy vs falsy values ===")
# Falsy: 0, 0.0, "", [], (), {}, set(), None, False
# Truthy: everything else
for value in [0, "", [], None, False, 42, "hi", [1]]:
    if value:
        print(f"Truthy: {value!r}")
    else:
        print(f"Falsy : {value!r}")

if not "":
    print("Empty string is falsy")
