# ============================================
# OOP - CLASSES
# ============================================

print("=== 1. Basic class with a method ===")
class A:
    def add(self, a, b):     # method - needs 'self' as first param
        return a + b

x = A()                      # instantiation -> instance of a class
print("x.add(1, 2):", x.add(1, 2))     # calling a method on an object

print("\n=== 2. Function vs Method ===")
# Using functions: add(x) - regular, needs only the needed arguments, no self
def add(a, b):
    return a + b

print("function add(1, 2):", add(1, 2))

# In methods: add(x) - needs 'self', an implicit reference to the object
# Method - needs an "object" on this side (self)
# Function - does not need an object
print("method A.add needs self; function add does not.")

print("\n=== 3. Class basics: __init__ ===")
class Person:
    def __init__(self, name):          # constructor, runs on instantiation
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Von")
p.greet()

print("\n=== 4. All methods are functions, but not all functions are methods ===")
# def for functions; keyword def with 'self' = methods
# Functions -> global; Methods -> attached to a class
print("check: callable(Person.greet) ->", callable(Person.greet))

print("\n=== 5. Argument rules (same as functions) ===")
# add(1, 2)     -> positional argument
# add(a=1, b=3) -> keyword argument
# add(b=2, a=3) -> keyword order doesn't matter
# add(b=2, 3)   -> ERROR: keyword dapat lahat ng sunod (positional after keyword)
# add(3, b=2)   -> legal
print("positional + keyword is fine: add(3, b=2) =", add(3, b=2))
# print(add(b=2, 3))   # ERROR: positional argument follows keyword argument

print("\n=== 6. Method Overloading vs Overriding ===")
# Method overloading -> same class
#    -> multiple methods: different return types / number of parameters
#    Python does not support true overloading (last def wins)
# Method overriding -> different classes, same function name
#    -> child class overrides the parent's method
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):                   # overrides Animal.speak
        return "Woof!"

print("Animal().speak():", Animal().speak())
print("Dog().speak():", Dog().speak())

print("\n=== 7. Decorators ===")
# @decorator -> ginagamit natin sa isang class/attribute/method
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

class Greeter:
    @shout                        # decorator applied to greet
    def greet(self, name):
        return f"Hello, {name}"

g = Greeter()
print(g.greet("von"))             # HELLO, VON
