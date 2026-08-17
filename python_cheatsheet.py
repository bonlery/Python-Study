# ============================================
# PYTHON CHEATSHEET
# Quick reference - no real lesson, just a
# commented summary of the core topics.
# ============================================

# --- Variables -------------------------------------------------
# name = value           assign a value to a variable
# Names can hold int, float, str, bool, and more.
name = "Von"             # str
age = 21                 # int
gpa = 1.2                # float
enrolled = True          # bool

# --- Operators ------------------------------------------------
# Arithmetic: + - * / // % **
# Comparison: == != < > <= >=
# Logical:    and or not
# Membership: in, not in
# Identity:   is, is not
# Assignment: = += -= *= /= //= %= **=

# --- Data types ------------------------------------------------
# int, float, str, bool
# list   -> mutable, ordered:      [1, 2, 3]
# tuple  -> immutable, ordered:    (1, 2, 3)
# dict   -> mutable, key-value:    {'a': 1}
# set    -> mutable, unique:       {1, 2, 3}
# None   -> null value

# --- Conditionals ----------------------------------------------
# if cond: ...
# elif cond: ...
# else: ...
# value_if_true if cond else value_if_false   (ternary)

# --- Loops -----------------------------------------------------
# for i in range(10): ...       0..9
# for i in range(1, 10): ...    1..9
# for i in range(1, 10, 2): ... step of 2
# for x in iterable: ...
# while cond: ...
# break / continue / pass
# else on loops: runs only when no break

# --- Functions ------------------------------------------------
# def f(a, b=default): return ...
# *args  -> extra positional args as a tuple
# **kwargs -> extra keyword args as a dict
# lambda a, b: a + b     nameless one-line function
# filter(lambda, iterable)  keep items passing the condition
# map(lambda, iterable)     transform every item

# --- Collections ----------------------------------------------
# list: append, extend, insert, pop, remove, del, index, count, sort
# dict: keys, values, items, get, pop, update
# set:  add, update, remove, discard, pop, clear, union |, &, -, ^
# str:  upper, lower, title, capitalize, strip, split, join,
#       replace, find, count, startswith, endswith
# slicing: seq[start:stop:step]

# --- String methods -------------------------------------------
# s.upper(), s.lower(), s.title(), s.capitalize()
# s.strip(), s.replace(old, new)
# s.split(sep), sep.join(list)
# s.find(sub), s.count(sub)
# s.startswith(x), s.endswith(x)

# --- Built-in functions ---------------------------------------
# print, input, len, sum, min, max, abs, round, pow
# sorted, reversed, enumerate, zip, range
# type, id, isinstance
# list, tuple, set, dict, int, float, str
# any, all

# --- File modes -----------------------------------------------
# 'r'  read (default)
# 'w'  write (overwrite/create)
# 'a'  append (add to end)
# 'x'  exclusive create (error if exists)
# open(path, mode) / with open(path, mode) as f:

# --- Exception handling ---------------------------------------
# try: ...
# except SpecificError: ...
# except: ...            (bare catch-all)
# else: ...              runs only if NO exception
# finally: ...           always runs
# raise ValueError("msg")  to raise your own error

# --- OOP syntax ------------------------------------------------
# class MyClass:
#     def __init__(self, arg): self.arg = arg
#     def method(self): ...
# obj = MyClass(value)
# obj.method()
# class Child(Parent): ...         inheritance
# @decorator                       decorators
# self = implicit reference to the object

# --- Scope -----------------------------------------------------
# LEGB: Local -> Enclosing -> Global -> Built-in
# global x  -> use the global variable inside a function

# --- Cheatsheet has no runnable output -------------------------
print("Cheatsheet loaded. Reference only - no execution output.")
