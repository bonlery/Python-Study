# ============================================
# SELF QUIZ - test yourself on the reviewer topics
# Multiple choice + output prediction.
# Questions come in random order every run.
# Usage:  python self_quiz.py
# Enter 'q' anytime to quit.
# ============================================

import random
import sys

# --- Question bank -------------------------------------------------
# Each question has: topic, q, why
# plus either:
#   options + answer (index of the correct option),  OR
#   answer (the expected free-text answer)
QUESTIONS = [
    # ---- errors ----
    {"topic": "errors",
     "q": "What error does this raise:  '123'.len() ?",
     "options": ["AttributeError", "TypeError", "ValueError", "SyntaxError"],
     "answer": 0,
     "why": "A str has no .len() method. Use the built-in len('123')."},
    {"topic": "errors",
     "q": "names = {'s1': 'Rijs'};  names['s5']  ->  what error?",
     "options": ["IndexError", "KeyError", "ValueError", "NameError"],
     "answer": 1,
     "why": "'s5' is not a key in the dict, so Python raises KeyError."},
    {"topic": "errors",
     "q": "[8, 3][3]  ->  what error?",
     "options": ["KeyError", "ValueError", "IndexError", "TypeError"],
     "answer": 2,
     "why": "The list only has indexes 0 and 1; index 3 is out of range."},
    {"topic": "errors",
     "q": "x = 5;  print(x + 'a')  ->  what error?",
     "options": ["ValueError", "TypeError", "NameError", "ZeroDivisionError"],
     "answer": 1,
     "why": "You cannot add an int and a str - incompatible types."},
    {"topic": "errors",
     "q": "int('hello')  ->  what error?",
     "options": ["TypeError", "KeyError", "ValueError", "AttributeError"],
     "answer": 2,
     "why": "'hello' is not a valid number, so int() raises ValueError."},

    # ---- exceptions ----
    {"topic": "exceptions",
     "q": "Which is the parent of BOTH KeyError and IndexError?",
     "options": ["ArithmeticError", "LookupError", "BaseException", "ValueError"],
     "answer": 1,
     "why": "LookupError is the parent of KeyError and IndexError."},
    {"topic": "exceptions",
     "q": "What is the parent of ZeroDivisionError?",
     "options": ["LookupError", "ValueError", "ArithmeticError", "KeyboardInterrupt"],
     "answer": 2,
     "why": "ZeroDivisionError is a child of ArithmeticError."},
    {"topic": "exceptions",
     "q": "In try/except, when does the else: block run?",
     "options": ["Always", "Only when an exception occurred",
                 "Only when NO exception occurred", "Only if there is a finally"],
     "answer": 2,
     "why": "else runs only when no exception happened; finally always runs."},
    {"topic": "exceptions",
     "q": "In try/except, when does the finally: block run?",
     "options": ["Only on error", "Only on success", "Always", "Never if except runs"],
     "answer": 2,
     "why": "finally always runs, no matter what."},

    # ---- collections ----
    {"topic": "collections",
     "q": "x = 1, 2  ->  what type is x?",
     "options": ["list", "tuple", "dict", "set"],
     "answer": 1,
     "why": "Commas make a tuple; the parentheses are optional."},
    {"topic": "collections",
     "q": "How do you make a tuple with ONE element?",
     "options": ["(5)", "[5]", "5,", "tuple(5)"],
     "answer": 2,
     "why": "A single-element tuple needs a trailing comma: 5,  is a tuple; (5) is just an int."},
    {"topic": "collections",
     "q": "lst = [1, 2, 3, 'a', True];  lst.append([1, 2])  ->  how many items now?",
     "options": ["5", "6", "7", "Error"],
     "answer": 1,
     "why": "append adds ONE item (the whole [1, 2] becomes one element). extend would add two."},
    {"topic": "collections",
     "q": "What's the difference between pop() and del?",
     "options": ["None, they are the same",
                 "pop() returns the removed item, del does not",
                 "del returns the item, pop does not",
                 "pop only works on dicts"],
     "answer": 1,
     "why": "pop() deletes AND returns the item; del removes it without returning."},
    {"topic": "collections",
     "q": "{} creates an empty...",
     "options": ["set", "list", "dict", "tuple"],
     "answer": 2,
     "why": "{} makes a dict. Use set() for an empty set."},
    {"topic": "collections",
     "q": "s = {1, 2, 3};  s.remove(99)  ->  what happens?",
     "options": ["Nothing", "KeyError", "99 is added", "ValueError"],
     "answer": 1,
     "why": "remove() errors if the item is missing. Use discard() when it may not exist."},
    {"topic": "collections",
     "q": "for i in names:  (names is a dict) iterates over...",
     "options": ["the values", "the keys", "(key, value) pairs", "random items"],
     "answer": 1,
     "why": "Iterating a dict directly gives its keys (same as names.keys())."},
    {"topic": "collections",
     "q": "for k, v in names.items():  iterates over...",
     "options": ["just the keys", "just the values", "(key, value) pairs", "key strings only"],
     "answer": 2,
     "why": "items() yields (key, value) tuples, which unpack into k, v."},

    # ---- slicing ----
    {"topic": "slicing",
     "q": "What is [1, 2, 3, 'a', True][::-1] ?",
     "answer": "[True, 'a', 3, 2, 1]",
     "why": "A step of -1 walks backwards, reversing the list."},
    {"topic": "slicing",
     "q": "What is 'Hello'[1:4] ?",
     "answer": "ell",
     "why": "Start at index 1 (e), stop BEFORE index 4 (o)."},
    {"topic": "slicing",
     "q": "What is [1, 2, 3, 4][2:0:-1] ?",
     "answer": "[3, 2]",
     "why": "Negative step: start at 2, walk down, stop before index 0."},
    {"topic": "slicing",
     "q": "lst = [1, 2, 3, 4];  lst[2:1] gives...",
     "options": ["an IndexError", "an empty list", "[2]", "[3, 2]"],
     "answer": 1,
     "why": "A slice where start >= stop with a positive step is empty - no error."},

    # ---- strings ----
    {"topic": "strings",
     "q": "Strings are immutable. To change 'hello' into 'Hello' you must...",
     "options": ["s[0] = 'H'", "use s.upper() then assign",
                 "create a new string: 'H' + s[1:]", "strings can be edited in place"],
     "answer": 2,
     "why": "'H' + s[1:] builds a new string. s[0] = 'H' would raise a TypeError."},

    # ---- loops / ternary / range ----
    {"topic": "loops",
     "q": "list(range(1, 10, 2)) is...",
     "answer": "[1, 3, 5, 7, 9]",
     "why": "start=1, stop=10 (exclusive), step=2."},
    {"topic": "loops",
     "q": "In a for/while loop, the else: block runs when...",
     "options": ["always", "the loop ends with break",
                 "the loop ends WITHOUT break", "never"],
     "answer": 2,
     "why": "loop-else runs only when the loop finishes without a break."},
    {"topic": "loops",
     "q": "break vs continue: which one skips the rest of the CURRENT iteration?",
     "options": ["break", "continue", "pass", "else"],
     "answer": 1,
     "why": "continue skips the rest of the current iteration; break exits the whole loop."},
    {"topic": "loops",
     "q": "'adult' if 15 >= 18 else 'minor' evaluates to...",
     "answer": "minor",
     "why": "Ternary: value-if-true if condition else value-if-false. 15 >= 18 is False."},
    {"topic": "loops",
     "q": "Which of these are all FALSY in Python?",
     "options": ["0, '', [], None", "1, '', [], True", "0, 'a', {}, 5", "[] only"],
     "answer": 0,
     "why": "Falsy: 0, 0.0, '', [], (), {}, set(), None, False. Everything else is truthy."},

    # ---- precedence ----
    {"topic": "precedence",
     "q": "What is -3 ** 2 ?",
     "answer": "-9",
     "why": "** binds tighter than unary minus, so it is -(3**2) = -9, not 9."},
    {"topic": "precedence",
     "q": "What is 2 ** 3 ** 2 ?",
     "answer": "512",
     "why": "** is right-to-left: 2 ** (3 ** 2) = 2 ** 9 = 512."},
    {"topic": "precedence",
     "q": "Which binds tighter:  and  or  or ?",
     "options": ["or", "and", "they are equal", "it depends"],
     "answer": 1,
     "why": "Order: not > and > or. So True or True and False is True or (True and False)."},
    {"topic": "precedence",
     "q": "What is True or True and False ?",
     "answer": "True",
     "why": "and first: True and False = False; then True or False = True."},
    {"topic": "precedence",
     "q": "What is 8 & 5 ^ 2 | 1 ?",
     "answer": "3",
     "why": "Bitwise order & then ^ then |: 8&5=0, 0^2=2, 2|1=3."},

    # ---- functions ----
    {"topic": "functions",
     "q": "def add(a=1, b=2): return a + b   ->   add() is...",
     "answer": "3",
     "why": "Both defaults are used: 1 + 2 = 3."},
    {"topic": "functions",
     "q": "Why is  def f(a=1, b):  invalid?",
     "options": ["Python doesn't allow defaults",
                 "a parameter after a default value must ALSO have a default",
                 "b must be *args",
                 "you need a return statement"],
     "answer": 1,
     "why": "Once a parameter has a default, every following parameter needs one too."},
    {"topic": "functions",
     "q": "def add(a=1, b=2): ...   add(b=2, 3)  ->  what happens?",
     "options": ["works, returns 5", "SyntaxError",
                 "TypeError: positional argument follows keyword argument",
                 "b silently gets 3"],
     "answer": 2,
     "why": "After a keyword argument, the rest must be keyword too: add(3, b=2) is fine."},
    {"topic": "functions",
     "q": "*args collects extra positional arguments into a...",
     "options": ["list", "tuple", "dict", "set"],
     "answer": 1,
     "why": "*args is a tuple of all extra positional arguments."},
    {"topic": "functions",
     "q": "**kwargs collects extra keyword arguments into a...",
     "options": ["tuple", "list", "dict", "string"],
     "answer": 2,
     "why": "**kwargs is a dict of name -> value pairs."},
    {"topic": "functions",
     "q": "What does LEGB stand for?",
     "options": ["Local, External, Global, Built-in",
                 "Local, Enclosing, Global, Built-in",
                 "List, Enum, Global, Built-in",
                 "Local, Enclosing, Generic, Base"],
     "answer": 1,
     "why": "Python looks up a name in that order: Local -> Enclosing -> Global -> Built-in."},
    {"topic": "functions",
     "q": "To MODIFY a global variable inside a function, use the...",
     "options": ["global keyword", "nonlocal keyword", "nothing - just assign", "return statement"],
     "answer": 0,
     "why": "Without 'global', assigning inside a function creates a local variable instead."},

    # ---- lambda / filter / map ----
    {"topic": "lambda",
     "q": "list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])) is...",
     "answer": "[2, 4, 6]",
     "why": "filter keeps only the items where the condition is True."},
    {"topic": "lambda",
     "q": "list(map(lambda n: n * 2, [1, 2, 3])) is...",
     "answer": "[2, 4, 6]",
     "why": "map transforms EVERY item."},
    {"topic": "lambda",
     "q": "filter vs map - the core difference is...",
     "options": ["none, they are the same",
                 "filter transforms every item, map keeps the passing ones",
                 "filter keeps items passing the condition, map transforms every item",
                 "map returns a dict"],
     "answer": 2,
     "why": "filter filters (keeps passing items); map transforms (every item)."},

    # ---- comprehensions ----
    {"topic": "comprehensions",
     "q": "[i ** 2 for i in range(4)] is...",
     "answer": "[0, 1, 4, 9]",
     "why": "Squares of 0, 1, 2, 3."},
    {"topic": "comprehensions",
     "q": "[n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0] is...",
     "answer": "[2, 4, 6]",
     "why": "A comprehension with a condition keeps only the evens."},

    # ---- identity / copying ----
    {"topic": "copying",
     "q": "a = [1, 2, 3];  b = a;  b.append(4)  ->  what is a now?",
     "answer": "[1, 2, 3, 4]",
     "why": "b = a does NOT copy - b references the SAME list, so a changed too."},
    {"topic": "copying",
     "q": "x = [1, 2];  y = [1, 2]  ->  x is y ?",
     "options": ["True", "False", "Error", "Depends on the values"],
     "answer": 1,
     "why": "is compares identity (same object); == compares value. x and y are different objects."},
    {"topic": "copying",
     "q": "a = [[1, 2], [3, 4]];  b = a.copy();  b[0].append(9)  ->  what is a[0]?",
     "answer": "[1, 2, 9]",
     "why": "copy() is shallow: the top list is copied but the inner lists are SHARED."},

    # ---- OOP ----
    {"topic": "oop",
     "q": "What must the first parameter of every instance method be?",
     "options": ["cls", "self", "this", "obj"],
     "answer": 1,
     "why": "Methods need self - the implicit reference to the object."},
    {"topic": "oop",
     "q": "When does __init__ run?",
     "options": ["When the class is defined",
                 "When an object is instantiated",
                 "When the object is deleted",
                 "Never automatically"],
     "answer": 1,
     "why": "__init__ is the constructor; it runs each time you create an instance."},
    {"topic": "oop",
     "q": "Method OVERRIDING means the same method name in...",
     "options": ["the same class (different params)",
                 "different classes - the child redefines the parent's method",
                 "different modules",
                 "only with a @decorator"],
     "answer": 1,
     "why": "Overriding happens across classes (child vs parent). Overloading (same class, different params) is not truly supported in Python."},
]

# --- helpers -------------------------------------------------------

def normalize(text):
    """Make two answers comparable: lowercase, no quotes, no spaces."""
    return "".join(str(text).strip().strip("'\"").split()).lower()


def read_input(prompt):
    """Read input; return 'q' sentinel on quit, None on EOF."""
    try:
        value = input(prompt)
    except EOFError:
        return None
    if value.strip().lower() in ("q", "quit"):
        return "QUIT"
    return value


def pick_count(total):
    prompt = f"How many questions? (Enter for all {total}): "
    while True:
        value = read_input(prompt)
        if value == "QUIT":
            return None
        if value is None or value.strip() == "":
            return total
        try:
            n = int(value.strip())
            if 1 <= n <= total:
                return n
        except ValueError:
            pass
        print(f"  Please enter a number from 1 to {total}, or Enter for all.")


def pick_topic():
    topics = sorted({q["topic"] for q in QUESTIONS})
    print("\nTopics:")
    for i, t in enumerate(topics, 1):
        print(f"  {i:>2}. {t}")
    print("   0. ALL topics")
    while True:
        value = read_input("\nPick a topic (number): ")
        if value == "QUIT":
            return None
        if value is None or value.strip() == "":
            return None   # empty = all topics
        try:
            n = int(value.strip())
        except ValueError:
            print("  Please enter a number.")
            continue
        if n == 0:
            return None
        if 1 <= n <= len(topics):
            return topics[n - 1]
        print(f"  Please enter a number from 0 to {len(topics)}.")


def ask_mcq(q):
    print("\nOptions:")
    for i, opt in enumerate(q["options"], 1):
        print(f"  {i}. {opt}")
    while True:
        value = read_input("Your choice (number): ")
        if value == "QUIT":
            return "QUIT"
        if value is None:
            return "QUIT"
        try:
            n = int(value.strip())
        except ValueError:
            print("  Please enter the option number.")
            continue
        if 1 <= n <= len(q["options"]):
            return n - 1
        print(f"  Please enter a number from 1 to {len(q['options'])}.")


def ask_free(q):
    value = read_input("Your answer: ")
    if value == "QUIT" or value is None:
        return "QUIT"
    return value


def run_quiz(pool):
    correct = 0
    breakdown = {}
    for i, q in enumerate(pool, 1):
        print(f"\n----------------------------------------")
        print(f"Question {i}:  [{q['topic']}]")
        print(f"  {q['q']}")
        if "options" in q:
            choice = ask_mcq(q)
            if choice == "QUIT":
                break
            user_answer = q["options"][choice]
            is_right = choice == q["answer"]
            right_answer = q["options"][q["answer"]]
        else:
            user_answer = ask_free(q)
            if user_answer == "QUIT":
                break
            is_right = normalize(user_answer) == normalize(q["answer"])
            right_answer = q["answer"]

        mark = "CORRECT" if is_right else "WRONG"
        print(f"  [{mark}]")
        print(f"  You said:  {user_answer}")
        if not is_right:
            print(f"  Correct:   {right_answer}")
        print(f"  Why: {q['why']}")

        if is_right:
            correct += 1
            breakdown[q["topic"]] = breakdown.get(q["topic"], 0) + 1

    return correct, len(pool)


def main():
    print("============================================")
    print(" SELF QUIZ - reviewer topics, random order")
    print(" Enter 'q' anytime to quit")
    print("============================================")

    topic = pick_topic()
    if topic == "QUIT":
        return
    pool = QUESTIONS if topic is None else [q for q in QUESTIONS if q["topic"] == topic]

    count = pick_count(len(pool))
    if count is None:
        return

    random.shuffle(pool)
    pool = pool[:count]

    correct, total = run_quiz(pool)

    print("\n============================================")
    print(f" FINAL SCORE: {correct} / {total}")
    if total:
        pct = round(100 * correct / total)
        print(f" ({pct}%)")
    if correct == total and total:
        print(" Perfect! You know this material.")
    print("============================================")


if __name__ == "__main__":
    main()
