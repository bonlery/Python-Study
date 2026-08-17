# ============================================
# ITERATION OVER DICTIONARIES
# ============================================

names = {
    's1': ['Rijs', 'Palugna'],
    's2': ['Mark', 'Mallari'],
    's3': ['John', 'Vicente']
}

print("=== 1. for i in names  -> prints KEYS ===")
for i in names:
    print(i)

print("\n=== 2. for i in names.values()  -> prints VALUES ===")
for i in names.values():
    print(i)

print("\n=== 3. for i in names.keys()  -> prints KEYS ===")
for i in names.keys():
    print(i)

print("\n=== 4. values: first and last name ===")
for i in names.values():
    print(i[0], i[-1])

print("\n=== 5. for i in names.items()  -> key-value pairs ===")
for key, value in names.items():
    print(f"{key}: {value}")

print("\n=== 6. Note ===")
print("for i in names: is the same as for i in names.keys():")
