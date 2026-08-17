# ============================================
# LISTS, TUPLES, DICTIONARIES
# ============================================

print("=== 1. Declaration ===")
lst = [1, 2, 3]        # list  -> mutable (can change)
tuples = ()            # tuple -> immutable (cannot change)
dicts = {}             # dict  -> key-value pair, mutable
print("list:", lst)
print("empty tuple:", tuples)
print("empty dict:", dicts)

print("\n=== 2. Tuple notes ===")
# Parentheses are optional: x = 1, 2  is a tuple
x = 1, 2
print("x = 1, 2 ->", x, "| type:", type(x))

# Single element tuple needs a trailing comma
x = 1,
print("x = 1, ->", x, "| type:", type(x))

# x = [1]  is a LIST, not a tuple
y = [1]
print("[1] is a", type(y).__name__, "not a tuple")

# Tuples support ACCESSING only (no item assignment)
t = (1, 2, 5, True, 'a')
print("t[1] =", t[1])
# t[0] = 3        # ERROR: 'tuple' object does not support item assignment

# To modify, convert: list -> edit -> tuple (defeats the purpose of a tuple)
t_list = list(t)
t_list[0] = 99
t = tuple(t_list)
print("after convert-edit-convert:", t)

# Any collection type can be HETEROGENEOUS (mixed types)
x = 1, 2, 5, True, 'a'
print("heterogeneous tuple:", x)
print("x[1:-1]:", x[1:-1])       # (2, 5, True)

print("\n=== 3. Dictionary notes ===")
names = {
    's1': ['Rijs', 'Palugna'],
    's2': ['Mark', 'Mallari'],
    's3': ['John', 'Vicente']
}
print("names['s3'][0]:", names['s3'][0])     # John

# Adding a key
names['s4'] = ['Sci', 'Dela Rosa']
print("after adding s4:", names)

# Updating (mutable) and deleting
names['s1'] = ['Chris', 'Bernardino']
names.pop('s2')
print("after update s1 + pop s2:", names)
