# ============================================
# VARIABLE SCOPE
# ============================================

print("=== 1. Local variables ===")
def my_func():
    local_var = 10          # local: only exists inside this function
    print("inside function, local_var =", local_var)

my_func()
# print(local_var)          # ERROR: NameError - local_var not defined outside

print("\n=== 2. Global variables ===")
global_var = 100            # global: defined at the top level

def show_global():
    print("reading global_var inside function:", global_var)

show_global()
print("reading global_var outside:", global_var)

print("\n=== 3. global keyword ===")
counter = 0

def increment():
    global counter          # tells Python to use the global counter
    counter += 1

increment()
increment()
print("counter after two increments:", counter)

# Without 'global' this would ERROR:
# def bad():
#     counter += 1          # ERROR: local 'counter' referenced before assignment

print("\n=== 4. LEGB scope explanation ===")
print("""LEGB - the order Python searches for a name:
  L - Local      (inside the current function)
  E - Enclosing  (outer functions / nested functions)
  G - Global     (module level)
  B - Built-in   (Python's built-in names like len, print)""")

# Enclosing example
def outer():
    x = "enclosing"

    def inner():
        print("inner sees:", x)     # found in the enclosing scope
    inner()

outer()

print("\n=== 5. Mutable vs immutable inside functions ===")
# Immutable (int, str, tuple): changes do NOT affect the original
def change_immutable(n):
    n = n + 1
    print("inside:", n)

val = 5
change_immutable(val)
print("outside, val is still:", val)

# Mutable (list, dict, set): changes DO affect the original
def change_mutable(lst):
    lst.append(99)

items = [1, 2, 3]
change_mutable(items)
print("outside, items now:", items)

# To avoid mutating, pass a copy
def safe_change(lst):
    lst = list(lst)          # local copy
    lst.append(99)

original = [1, 2, 3]
safe_change(original)
print("with a copy, original stays:", original)
