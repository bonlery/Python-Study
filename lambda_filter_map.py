# ============================================
# LAMBDA, filter, map
# ============================================

print("=== 1. Lambda (nameless function) ===")
# lambda is a nameless/one-line function
x = lambda a, b: a + b
print("x = lambda a, b: a + b -> x(1, 2) =", x(1, 2))

# Note: assigning a lambda to a variable defeats its purpose.
# Better: use it directly where a function is expected.
print("(lambda a, b: a + b)(5, 3):", (lambda a, b: a + b)(5, 3))

print("\n=== 2. filter ===")
# filter -> 1st param is a lambda, 2nd param is an iterable
#          ireturn lahat yung pasok sa condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("even numbers:", evens)

small = list(filter(lambda n: n < 5, numbers))
print("numbers < 5:", small)

print("\n=== 3. map ===")
# map -> same signature (lambda, iterable)
#       ireturn lahat, may transformation applied
doubled = list(map(lambda n: n * 2, numbers))
print("n * 2:", doubled)

squared = list(map(lambda n: n ** 2, numbers))
print("n ** 2:", squared)

names = ['rijis', 'mark', 'john']
titled = list(map(lambda name: name.title(), names))
print("names .title():", titled)

print("\n=== 4. filter vs map - the difference ===")
print("filter -> returns only the items that PASS the condition")
print("map    -> returns ALL items with a transformation applied")

# filter keeps some items (condition must be true)
# map transforms every item
data = [1, 2, 3, 4]
print("filter even:", list(filter(lambda n: n % 2 == 0, data)))   # [2, 4]
print("map * 10:  ", list(map(lambda n: n * 10, data)))           # [10, 20, 30, 40]
