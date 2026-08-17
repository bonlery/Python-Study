# ============================================
# EXCEPTION HIERARCHY + EXCEPTION HANDLING
# ============================================

# --- EXCEPTION HIERARCHY (reference) ---------------------------
# BaseException
#  |-- Exception
#  |    |-- ArithmeticError
#  |    |    `-- ZeroDivisionError
#  |    |-- LookupError
#  |    |    |-- KeyError
#  |    |    `-- IndexError
#  |    |-- ValueError
#  |    `-- ... (everything up to LookupError level is under Exception)
#  `-- KeyboardInterrupt
#
# - LookupError is the parent of KeyError and IndexError
# - ArithmeticError is the parent of ZeroDivisionError
# - ValueError up to LookupError are all children of Exception
# - KeyboardInterrupt and Exception are both children of BaseException
# - The most general catch-all is BaseException
# ================================================================

print("=== 1. Basic try/except ===")
try:
    print(1 / 0)
except:
    print('Mali')          # bare except catches everything

print("\n=== 2. Multiple except blocks ===")
try:
    print(1 / 0)
except ZeroDivisionError:
    print('Mali')          # specific error first
except ArithmeticError:
    print('mali')          # parent error next
except:
    print(0)               # fallback catch-all

print("\n=== 3. else and finally ===")
try:
    print(1 / 0)
except ZeroDivisionError:
    print('Mali')
else:
    print('Hello')         # runs only if NO exception occurred
finally:
    print('Tapos na')      # always runs, no matter what

print("\n=== 4. else only runs when no error ===")
try:
    print(2 + 2)
except ZeroDivisionError:
    print('Mali')
else:
    print('Hello')         # runs because no exception happened
finally:
    print('Tapos na')      # always runs

print("\n=== 5. Catching the exception object ===")
try:
    print([8, 3][5])
except IndexError as e:
    print("Caught:", e)

print("\n=== Tip ===")
print("Find the specific/appropriate error keyword for the error you'll encounter.")
