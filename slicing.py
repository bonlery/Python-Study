# ============================================
# SLICING
# ============================================

lst = [1, 2, 3, 'a', True]
# Positive index:   0   1   2    3     4
# Negative index:  -5  -4  -3   -2    -1

print("=== 1. Basic slicing  start:stop ===")
print("lst[1:3]:", lst[1:3])         # [2, 3]
print("lst[1:]:", lst[1:])           # [2, 3, 'a', True]
print("lst[:3]:", lst[:3])           # [1, 2, 3]
print("lst[:]:", lst[:])             # copy of the whole list

print("\n=== 2. Negative indexing ===")
print("lst[-1]:", lst[-1])           # True
print("lst[-3]:", lst[-3])           # 3

print("\n=== 3. Empty slice ===")
print("lst[2:1]:", lst[2:1])         # walang error, walang output (empty slice)

print("\n=== 4. Step ===")
print("lst[::2]:", lst[::2])         # every 2nd item: [1, 3, True]
print("lst[2:0:-1]:", lst[2:0:-1])   # [3, 2] - step -1 goes backwards
print("lst[::-1]:", lst[::-1])       # reverse the list

print("\n=== 5. Slicing strings ===")
a = 'Hello'
print("a[::-1]:", a[::-1])           # 'olleH'
print("a[1:4]:", a[1:4])             # 'ell'
print("a[::2]:", a[::2])             # 'Hlo'

print("\n=== 6. Slicing tuples ===")
t = (1, 2, 5, True, 'a')
print("t[1:-1]:", t[1:-1])           # (2, 5, True)

print("\n=== 7. Note ===")
print("lst[2:1] gives an empty list, NOT an error.")
