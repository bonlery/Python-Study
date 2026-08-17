# ============================================
# OPERATOR PRECEDENCE (complete table)
# Highest precedence = evaluated first
# ============================================

print("=== Complete Order of Precedence (highest to lowest) ===")
print(" 1. (expr), [expr], {expr}      grouping / containers")
print(" 2. x[i], x[i:j], f(args), x.attr   subscript, slice, call, attribute")
print(" 3. **                          exponent (RSB - right-to-left)")
print(" 4. +x, -x, ~x                  unary plus, minus, bitwise NOT")
print(" 5. *, /, //, %, @              multiply, divide, floor, mod, matmul")
print(" 6. +, -                        addition, subtraction")
print(" 7. <<, >>                      bitwise shifts (left-to-right)")
print(" 8. &                           bitwise AND")
print(" 9. ^                           bitwise XOR")
print("10. |                           bitwise OR")
print("11. ==, !=, <, <=, >, >=, in, not in, is, is not")
print("    comparisons, membership, identity")
print("12. not                          boolean NOT")
print("13. and                          boolean AND")
print("14. or                           boolean OR")
print("Note: ternary  x if C else y, lambda, and :=  bind loosest of all.")

print("\n=== Arithmetic: 1-6 ===")
print("7 + 3 * 2 ** 2 // 3 % 5")
print("Steps:")
print("  2 ** 2 = 4        (exponent first)")
print("  3 * 4  = 12       (multiply)")
print("  12 // 3 = 4       (floor divide)")
print("  4 % 5 = 4         (modulo)")
print("  7 + 4 = 11")
print("Result:", 7 + 3 * 2 ** 2 // 3 % 5)

print("\n=== Parentheses override precedence ===")
print("(7 + 3) * 2 ** 2 // 3 % 5 =", (7 + 3) * 2 ** 2 // 3 % 5)

print("\n=== Unary before multiplicative ===")
print("-3 ** 2 =", -3 ** 2)              # -(3**2) = -9
print("(-3) ** 2 =", (-3) ** 2)          # 9
print("~3 * 2 =", ~3 * 2)                # -4 * 2 = -8

print("\n=== Bitwise order: & before ^ before | ===")
print("8 & 5 ^ 2 | 1")
print("Steps:")
print("  8 & 5  = 0        (AND first)")
print("  0 ^ 2  = 2        (XOR)")
print("  2 | 1  = 3        (OR)")
print("Result:", 8 & 5 ^ 2 | 1)

print("\n=== Shift is left-to-right (not RSB) ===")
print("32 >> 2 >> 1 =", 32 >> 2 >> 1)    # (32>>2)>>1 = 8>>1 = 4

print("\n=== Comparison before not/and/or ===")
print("not 5 > 3 ->", not 5 > 3)         # not True = False
print("2 + 2 == 4 and 1 < 2 ->", 2 + 2 == 4 and 1 < 2)

print("\n=== and binds tighter than or ===")
print("True or True and False ->", True or True and False)  # True or (True and False)

print("\n=== Comparison chain (chained, not grouped) ===")
print("1 < 2 < 3 ->", 1 < 2 < 3)         # True

print("\n=== Right-to-left for ** ===")
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)      # 2 ** (3 ** 2) = 512

print("\n=== Lowest: ternary / lambda / walrus ===")
print("1 + 2 if False else 3 + 4 ->", 1 + 2 if False else 3 + 4)   # 7
x = 0
print("(y := 10) + 5 ->", (y := 10) + 5)  # walrus needs parens to bind tightly
print("double = lambda n: n * 2; double(4) ->", (lambda n: n * 2)(4))
