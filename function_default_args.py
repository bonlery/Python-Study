# ============================================
# FUNCTIONS - DEFAULT VALUES & ARGUMENTS
# ============================================

print("=== 1. Default values ===")
def add(a=1, b=2):
    return a + b

print("add():", add())          # 3
print("add(b=3):", add(b=3))    # 4 - pwede dahil may value
print("add(a=3):", add(a=3))    # 5
print("add(2, 3):", add(2, 3))  # 5 - positional
print("add(a=1, b=4):", add(a=1, b=4))   # 5
print("add(b=1, a=9):", add(b=1, a=9))   # 10 - keyword order doesn't matter
print("add(4):", add(4))        # 6
print("add(2, b=4):", add(2, b=4))       # 6 - positional + keyword

# --- Error cases (commented out) ---
# add(2, a=4)                  # ERROR: two values for same parameter 'a'
# add(a=1, 2)                  # ERROR: positional after keyword

print("\n=== 2. Parameter rules ===")
print("def add(a=1, 2) is NOT allowed: a parameter after a")
print("   default value must ALSO have a default value.")
print("def add(a, b=1) IS ok: non-default parameter comes first.")

def add2(a, b=1):
    return a + b

print("add2(10):", add2(10))       # 11
print("add2(10, 5):", add2(10, 5)) # 15

print("\n=== 3. Positional vs Keyword args ===")
# add(1, 2)   -> positional argument, bawat arg ay isang parameter
# add(a=1, b=3) -> keyword argument
# add(b=2, a=3) -> keyword order doesn't matter
print("add(b=2, a=3):", add(b=2, a=3))   # 5

# add(b=2, 3)  -> ERROR: keyword dapat lahat ng sunod
#                 kapag nagsimula na sa keyword arg
# add(3, b=2)  -> legal (positional first, then keyword)
print("add(3, b=2):", add(3, b=2))       # 5
