# PYTHON REVIEWER

## 1. COMMON ERRORS
```python
print('123'.len())        # AttributeError
print(1/0)                # ZeroDivisionError
print(names['s5'])         # KeyError
print([8,3][3])            # IndexError - list index out of bounds
```
Common encountered errors: **Value**Error, **Type**Error, **Name**Error

```python
x = int(input())
input a -> ValueError            # e.g. non-numeric input
print(x + 'a')  # TypeError      # mixing incompatible types

def a(x):
pass   -> error -> IndentationError   # missing/incorrect indentation

def a(y=2  ]      # SyntaxError
    print(y)       # NameError   # undefined/mismatched variable
```

**KeyboardInterrupt** — happens if we force stop the program (e.g. Ctrl+C)

## 2. EXCEPTION HIERARCHY
```
BaseException
 └── Exception
      ├── ArithmeticError
      │     └── ZeroDivisionError
      ├── LookupError
      │     ├── KeyError
      │     └── IndexError
      ├── ValueError
      └── ... (up to LookupError level are all under Exception)

BaseException
 └── KeyboardInterrupt
 └── Exception
```
- `LookupError` is the parent of `KeyError` and `IndexError`
- `ArithmeticError` is the parent of `ZeroDivisionError`
- `ValueError` up to `LookupError` are all children of `Exception`
- `KeyboardInterrupt` and `Exception` are both children of `BaseException`

## 3. EXCEPTION HANDLING
```python
try:
    print(1/0)
except:
    print('Mali')
```

```python
try:
    print(1/0)
except ZeroDivisionError:
    print('Mali')
except ArithmeticError:
    print('mali')
except:
    print(0)
else:
    print('Hello')     # runs only if NO exception occurred
finally:
    print('Tapos na')  # always runs, no matter what
```

**Tip:** Find the specific/appropriate error keyword for the error you'll encounter.
The most general catch-all is `BaseException`.

## 4. LISTS, TUPLES, DICTIONARIES

### Declaration
```python
lst = [1, 2, 3]        # list  -> mutable
tuples = ()             # tuple -> immutable
dicts = {}               # dict  -> key-value pair, mutable
```

### Tuple notes
- Parentheses are optional: `x = 1, 2  # tuple`
- Single element tuple needs a trailing comma: `x = 1,  # tuple`
  - `x = [1]` is a **list**, not a tuple
- Tuples support **accessing only** (no item assignment)
  ```python
  x[0] = 3   # error
  ```
  - To modify, convert: `x = list(x)`, edit, then `x = tuple(x)` — but this defeats the purpose of a tuple
- Any collection type can be **heterogeneous**:
  ```python
  x = 1, 2, 5, True, 'a'
  print(x[1:-1])   # (2, 5, True)
  ```

### Dictionary notes
```python
names = {
    's1': ['Rijs', 'Palugna'],
    's2': ['Mark', 'Mallari'],
    's3': ['John', 'Vicente']
}
print(names['s3'][0])   # John

# Adding a key
names['s4'] = ['Sci', 'Dela Rosa']

# Since non-existent, mangdd the dict (dictionaries are mutable)
names['s1'] = ['Chris', 'Bernardino']
names.pop('s2')
```

## 5. ITERATION
```python
for i in names:
    print(i)          # prints keys

for i in names.values():
    print(i)

for i in names.keys():
    print(i)

for i in names.values():
    print(i[0], i[-1])

for i in names.items():
    print(f"{i}: {names[i]}")
```

## 6. SLICING
```python
lst = [1, 2, 3]
tuples = ()
dicts = {}

# Slicing
print(lst[1:3])     # start:stop

lst = [1, 2, 3, 'a', True]
# Positive index:   0   1  2   3     4
# Negative index:  -5  -4 -3  -2    -1

lst[2:1]      # walang error, walang output (empty slice)
lst[2:0:-1]

lst[:3]       # start from index 0, stop before index 3
lst[2:]       # start from index 2 until the end of the list
lst[::-1]     # reverse the list

a = 'Hello'
print(a[::-1])
```

## 7. CRUD ON LISTS
```
C - Create
R - Read
U - Update
D - Delete
```
```python
lst = [1, 2, 3, 'a', True]

# append
lst.append([1, 2])
print(lst)
# [1, 2, 3, 'a', True, [1, 2]]

lst.extend([1, 2])
# [1, 2, 3, 'a', True, [1, 2], 1, 2]

lst.insert(3, 'Hi')

# Update
lst[-1] = False

# Delete
lst.pop()          # deletes last item, returns it
del lst[0]         # remove item at index, does not return it

lst = [1, 2, 'a']
x = lst.pop(-3)

lst[1] = lst[1] * x

print(lst)          # [1, 'aa', True]

len(lst)             # length of list
```

## 8. TERNARY / SHORTHAND FOR LOOP
```python
{a if .2 f}          # ternary in Python

print(i, end=" ")

# Shorthand for loop
for loop:
range(10)  -> stop -> 0,1,2,3,4,5,6,7,8,9
range(1,10)  -> 1 to 9
range(1,10,2)
      start   stop  step

for i in range(10, 0, 2):
    print(i)
    # -> walang nangyayari, walang output, walang ring error
```

## 9. OPERATOR PRECEDENCE
```
1–5   Arithmetic
6–9   Bitwise
10–13 Comparison
```
**Order of Precedence**
1. `()`
2. `**`               (RSB - Right-to-left)
3. `~x, +x, -x`
4. `*, /, //, %`
5. `+, -`
6. `<<, >>`           (RSB - Right-to-left)
7. `&`
8. `^`
9. `|`
10. comparison, membership, identity
11. `not`
12. `and`
13. `or`

**Example evaluation:**
```
7 + 3 * 2 ** 2 // 3 % 5
     4
1 % 5 = 1
7 + 1 = 8
```

## 10. FUNCTIONS

### Default values
```python
def add(a=1, b=2):
    return a + b

add()             # 3
add(b=3)          # pwede dahil may value
add(a=3)
add(2, 3)
add(2, a=4)       # ERROR - two values for same parameter
add(a=1, b=4)
add(b=1, a=9)
add(4) = 6
add(2, b=4) = 6
```
**Error case:**
```python
def add(a=1, 2)          # not allowed
                          # parameter after default value
                          # must also have a default value
def add(a, b=1)          # ok - non-default param first
```

### *args and **kwargs
```python
*args  -> kukunin lahat ng parameters ng function
**kwargs

def add(*nums):
    return sum(nums)

add(2, 4, 6, 8, 10, 12) = 42

def add(1, 3, 5, 7, 9)
```
`**kwargs` = dictionary
```python
def info(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

info(fname='Paul', lname='Dela Rosa')
k, v = ('fname', 'Paul')
```

### Lambda
```python
x = lambda a, b: a + b
x(1, 2)    # defeats the purpose of lambda if assigned to a variable

# lambda is a nameless function
```

### filter vs map
```
filter -> first param is a lambda, 2nd param is an iterable (list, dict, str)
map    -> same

Difference:
filter -> ireturn lahat yung pasok sa condition
map    -> ireturn lahat, may transformation applied
```

## 11. OOP (CLASSES)

```python
class A:
    def add(self, a, b):     # method - needs 'self' as first param
        return a + b

x = A()          # instantiation, instance of a class
x.add(1, 2)      # calling a method on an object
```

- **Using functions**: `add(x)` — regular, needed argument lang, no `self`
- **In methods**: `add(x)` — need `self`, needs an implicit reference to the object
- Method - needs an "object" on this side (`self`)
- Function - does not need on an object

```python
add(1, 2)          -> positional argument, kada arg ay isang parameter
add(a=1, b=3)       -> keyword arg, hindi porket bawat parameter dapat
                        by keyword ang pagtaran ng value
add(b=2, a=3)       -> matching pag idedeclare ang keyword

add(b=2, 3)         -> keyword dapat lahat ng sunod
                        kapag nagsimula na sa keyword arg
add(3, b=2)         -> legal
```

### Method Overloading vs Overriding
```
Method overloading -> same class
    -> multiple: different return types
    -> number of parameters

Method overriding
    -> different classes, same function name
    -> child class overrides parent's method
```

### Decorators
```python
@override -> decorator ang gagawin natin sa isang class/attribute
```

### Class basics
```python
class A:
    def __init__(self):
        pass

class A:
    def g(self):
        pass
```
- All methods are functions, but not all functions are methods
- `def` for functions; keyword `def` for functions with `self` = methods
- Functions -> global; Methods -> attached to a class

```python
[-5.9, 7.3, '9', '3', ['A', '4', 'v', 0, 'h'], True]
```
