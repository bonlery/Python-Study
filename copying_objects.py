# ============================================
# COPYING OBJECTS
# ============================================

print("=== 1. Assignment vs copying ===")
a = [1, 2, 3]
b = a                      # b references the SAME list as a
b.append(99)
print("a:", a)             # [1, 2, 3, 99] - changed too!
print("b:", b)
print("a is b:", a is b)   # True - same object

print("\n=== 2. Shallow copies ===")
a = [1, 2, 3]
c = a.copy()               # copy() - new top-level list
c.append(99)
print("a:", a, "| c:", c)
print("a is c:", a is c)   # False - different objects

d = a[:]                   # slicing also makes a copy
d.append(100)
print("a:", a, "| d:", d)

e = list(a)                # list() constructor
e.append(1000)
print("a:", a, "| e:", e)

print("\n=== 3. Nested lists and shallow copies ===")
a = [[1, 2], [3, 4]]
b = a.copy()               # top level copied, but inner lists are SHARED
b[0].append(99)            # mutates the inner list
print("a:", a)             # [[1, 2, 99], [3, 4]] - inner list changed!
print("b:", b)
print("a[0] is b[0]:", a[0] is b[0])   # True - same inner object

print("\n=== 4. Deep copy ===")
import copy
a = [[1, 2], [3, 4]]
d = copy.deepcopy(a)       # copies everything, including nested lists
d[0].append(99)
print("a:", a)             # unchanged
print("d:", d)
print("a[0] is d[0]:", a[0] is d[0])   # False - fully independent

print("\n=== 5. Identity (is) vs equality (==) ===")
x = [1, 2, 3]
y = [1, 2, 3]
print("x == y:", x == y)   # True  - equal VALUES
print("x is y:", x is y)   # False - different OBJECTS
print("x is x:", x is x)   # True  - same object

z = x
print("z is x:", z is x)   # True  - assignment shares the object

print("\n=== 6. Rule of thumb ===")
print("Use == to compare VALUES, use is to compare IDENTITY.")
print("For nested structures that must be independent, use deepcopy().")
