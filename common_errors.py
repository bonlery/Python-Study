# ============================================
# COMMON ERRORS
# Each example shows what happens when it
# actually runs. Lines that raise errors are
# commented out with an explanation.
# ============================================

# --- AttributeError ---------------------------------------------
# '123'.len()              # AttributeError: 'str' has no attribute 'len'
print("AttributeError: 'str' has no method 'len' (use len('123'))")

# --- ZeroDivisionError -------------------------------------------
# print(1 / 0)            # ZeroDivisionError: division by zero
print("ZeroDivisionError: cannot divide by zero")

# --- KeyError ------------------------------------------------------
names = {"s1": "Rijs"}
# print(names['s5'])      # KeyError: 's5' is not a key in names
print("KeyError: 's5' is not a key in the dictionary")

# --- IndexError -----------------------------------------------------
# print([8, 3][3])        # IndexError: list index out of range
print("IndexError: list index out of bounds")

# --- ValueError ------------------------------------------------------
# x = int("hello")        # ValueError: invalid literal for int()
print("ValueError: cannot convert 'hello' to an int")

# --- TypeError -------------------------------------------------------
# x = 5
# print(x + 'a')          # TypeError: unsupported operand for + (int + str)
print("TypeError: mixing incompatible types (int + str)")

# --- NameError ---------------------------------------------------------
# print(y)                # NameError: y is not defined
print("NameError: name 'y' is not defined (mismatched/undefined variable)")

# --- IndentationError ----------------------------------------------------
# def a(x):
# pass                    # IndentationError: expected an indented block
print("IndentationError: missing/incorrect indentation")

# --- SyntaxError -----------------------------------------------------------
# def a(y=2 ]             # SyntaxError: invalid syntax (extra bracket)
print("SyntaxError: invalid syntax (e.g. unmatched bracket)")

# --- KeyboardInterrupt ------------------------------------------------------
# Happens if we force stop the program (e.g. Ctrl+C).
print("KeyboardInterrupt: raised when the program is force-stopped (Ctrl+C)")

# --- Summary ----------------------------------------------------------------
# Common encountered errors: ValueError, TypeError, NameError
print("\nCommon errors to remember: ValueError, TypeError, NameError")
