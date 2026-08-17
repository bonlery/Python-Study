# ============================================
# BUILT-IN FUNCTIONS
# ============================================

print("=== 1. print, input ===")
print("print is used to output")
# name = input("What's your name? ")   # try it yourself
print("input() reads a line from the user")

print("\n=== 2. type, id, isinstance ===")
x = 42
print("type(42):", type(x))
print("id(x):", id(x))
print("isinstance(42, int):", isinstance(42, int))
print("isinstance('hi', str):", isinstance('hi', str))
print("isinstance([], (list, tuple)):", isinstance([], (list, tuple)))

print("\n=== 3. len, sum, min, max, abs, round, pow ===")
nums = [5, 2, 9, 1, 7]
print("len(nums):", len(nums))
print("sum(nums):", sum(nums))
print("min(nums):", min(nums))
print("max(nums):", max(nums))
print("abs(-7):", abs(-7))
print("round(3.14159, 2):", round(3.14159, 2))
print("pow(2, 10):", pow(2, 10))
print("2 ** 10:", 2 ** 10)             # same as pow

print("\n=== 4. sorted, reversed ===")
print("sorted(nums):", sorted(nums))
print("sorted(nums, reverse=True):", sorted(nums, reverse=True))
print("list(reversed(nums)):", list(reversed(nums)))
print("''.join(reversed('abc')):", ''.join(reversed('abc')))

print("\n=== 5. enumerate, zip, range ===")
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
print("list(enumerate(fruits)):", list(enumerate(fruits)))

names = ['von', 'rijis', 'mark']
scores = [95, 88, 92]
print("list(zip(names, scores)):", list(zip(names, scores)))
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

print("list(range(3, 10, 2)):", list(range(3, 10, 2)))

print("\n=== 6. Type constructors ===")
print("list('abc'):", list('abc'))
print("tuple([1, 2, 3]):", tuple([1, 2, 3]))
print("set([1, 1, 2, 3]):", set([1, 1, 2, 3]))
print("dict([('a', 1), ('b', 2)]):", dict([('a', 1), ('b', 2)]))
print("int('5'):", int('5'))
print("float(2):", float(2))
print("str(123):", str(123))

print("\n=== 7. any, all ===")
print("any([False, False, True]):", any([False, False, True]))
print("all([True, True, True]):", all([True, True, True]))
print("any([]):", any([]))             # False
print("all([]):", all([]))             # True
nums2 = [2, 4, 6, 8]
print("all(n % 2 == 0 for n in nums2):", all(n % 2 == 0 for n in nums2))
