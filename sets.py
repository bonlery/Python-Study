# ============================================
# SETS
# ============================================

print("=== 1. Creating sets ===")
s = {1, 2, 3}
print("s:", s, "| type:", type(s))
empty = set()          # {} makes a dict, NOT a set
print("set():", empty)

print("\n=== 2. Removing duplicates ===")
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print("list:", numbers)
print("set:", unique)

print("\n=== 3. add, update, remove, discard, pop, clear ===")
s = {1, 2, 3}
s.add(4)
print("after add(4):", s)
s.update([5, 6])
print("after update([5, 6]):", s)
s.remove(2)
print("after remove(2):", s)
s.discard(99)          # discard does NOT error if missing
print("after discard(99) (missing):", s)
s.discard(1)
print("after discard(1):", s)
s.pop()                # removes an arbitrary element
print("after pop():", s)
s.clear()
print("after clear():", s)

# s.remove(99)         # ERROR: KeyError - 99 not in set (use discard)

print("\n=== 4. Membership testing ===")
s = {1, 2, 3}
print("2 in s:", 2 in s)
print("5 in s:", 5 in s)
print("5 not in s:", 5 not in s)

print("\n=== 5. Set operations ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("a:", a, "| b:", b)
print("union:", a | b, "or", a.union(b))
print("intersection:", a & b, "or", a.intersection(b))
print("difference (a - b):", a - b, "or", a.difference(b))
print("symmetric difference:", a ^ b, "or", a.symmetric_difference(b))

print("\n=== 6. Set comprehensions ===")
squares = {x ** 2 for x in range(6)}
print("squares:", squares)
evens = {x for x in range(10) if x % 2 == 0}
print("evens:", evens)
