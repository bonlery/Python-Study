# ============================================
# LIST COMPREHENSIONS
# ============================================

print("=== 1. Basic list comprehension ===")
# for-loop version
squares = []
for i in range(5):
    squares.append(i ** 2)
# comprehension version
squares2 = [i ** 2 for i in range(5)]
print("loop:", squares)
print("comp:", squares2)

print("\n=== 2. Conditional comprehensions ===")
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in nums if n % 2 == 0]
print("evens:", evens)

# for-loop equivalent
evens2 = []
for n in nums:
    if n % 2 == 0:
        evens2.append(n)
print("evens (loop):", evens2)

print("\n=== 3. if/else in comprehension ===")
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print("labels:", labels)

print("\n=== 4. Nested comprehensions ===")
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print("flattened:", flattened)

# nested loops equivalent
flat2 = []
for row in matrix:
    for num in row:
        flat2.append(num)
print("flattened (loops):", flat2)

print("\n=== 5. Dictionary comprehensions ===")
sq = {i: i ** 2 for i in range(1, 5)}
print("squares dict:", sq)

names = ["von", "rijis", "mark"]
caps = {name: name.upper() for name in names}
print("names dict:", caps)

print("\n=== 6. Set comprehensions ===")
unique = {x % 3 for x in range(10)}
print("x % 3 for 0..9:", unique)

print("\n=== 7. String operations in comprehension ===")
words = ["hello", "world", "python"]
lengths = [len(w) for w in words]
print("lengths:", lengths)
