# ============================================
# FUNCTIONS - *args and **kwargs
# *args  -> takes ALL positional parameters
# **kwargs -> takes all keyword parameters (as a dict)
# ============================================

print("=== 1. *args ===")
def add(*nums):
    return sum(nums)

print("add(2, 4, 6, 8, 10, 12):", add(2, 4, 6, 8, 10, 12))   # 42
print("add(1, 3, 5, 7, 9):", add(1, 3, 5, 7, 9))             # 25
print("add(5):", add(5))                                      # 5

def show_args(*args):
    print("args:", args, "| type:", type(args))

show_args(1, 2, 3)
show_args()                      # empty tuple

print("\n=== 2. **kwargs ===")
# **kwargs = dictionary
def info(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

info(fname='Paul', lname='Dela Rosa')
# k, v = ('fname', 'Paul')  <- items() yields these tuples

print("\n=== 3. Combining *args and **kwargs ===")
def full_info(title, *nums, **tags):
    print("title:", title)
    print("nums:", nums)
    print("tags:", tags)

full_info("A", 1, 2, 3, color="red", size=5)

print("\n=== 4. Note ===")
print("*args gathers extra positional args as a tuple,")
print("**kwargs gathers extra keyword args as a dictionary.")
