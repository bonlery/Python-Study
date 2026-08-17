# ============================================
# PREDICT-RUN TRAINER
# The core study method: predict the output
# BEFORE you see it, then run the code.
# Usage:  python predict_run.py
# Enter 'q' anytime to quit.
# ============================================

import contextlib
import io
import random
import sys

# --- Snippet bank --------------------------------------------------
# Each snippet is pure code that PRINTs exactly one answer line.
# The actual output is computed by running the snippet, so the
# "correct" answer is always generated, never hardcoded.
SNIPPETS = [
    # ---- precedence ----
    {"topic": "precedence",
     "code": "print(-3 ** 2)",
     "explain": "** binds tighter than unary minus: -(3**2) = -9, not 9."},
    {"topic": "precedence",
     "code": "print(2 ** 3 ** 2)",
     "explain": "** is right-to-left: 2 ** (3 ** 2) = 2 ** 9 = 512."},
    {"topic": "precedence",
     "code": "print(True or True and False)",
     "explain": "and binds tighter than or: True or (True and False) = True or False = True."},
    {"topic": "precedence",
     "code": "print(7 + 3 * 2 ** 2 // 3 % 5)",
     "explain": "2**2=4; 3*4=12; 12//3=4; 4%5=4; 7+4=11."},
    {"topic": "precedence",
     "code": "print(8 & 5 ^ 2 | 1)",
     "explain": "Bitwise order & then ^ then |: 8&5=0, 0^2=2, 2|1=3."},
    {"topic": "precedence",
     "code": "print(not 5 > 3)",
     "explain": "Comparison binds tighter than not: not (5 > 3) = not True = False."},
    {"topic": "precedence",
     "code": "print(3 + 2 << 1)",
     "explain": "Addition binds tighter than the shift: (3+2)<<1 = 5<<1 = 10."},
    {"topic": "precedence",
     "code": "print(2 * 3 ** 2)",
     "explain": "** first: 3**2=9, then 2*9=18."},

    # ---- slicing ----
    {"topic": "slicing",
     "code": "print([1, 2, 3, 'a', True][::-1])",
     "explain": "A step of -1 reverses the whole list."},
    {"topic": "slicing",
     "code": "print('Hello'[1:4])",
     "explain": "Start at index 1, stop BEFORE index 4."},
    {"topic": "slicing",
     "code": "print([1, 2, 3, 4][::2])",
     "explain": "Every 2nd item starting at index 0."},
    {"topic": "slicing",
     "code": "print([1, 2, 3, 'a', True][2:0:-1])",
     "explain": "Negative step walks backwards: start 2, stop before 0."},
    {"topic": "slicing",
     "code": "print('Python'[-3:])",
     "explain": "Negative index -3 counts from the end, so we get the last 3 chars."},
    {"topic": "slicing",
     "code": "print((1, 2, 5, True, 'a')[1:-1])",
     "explain": "Slicing works on tuples too."},

    # ---- strings ----
    {"topic": "strings",
     "code": "print('hello'.upper())",
     "explain": "upper() returns the string in uppercase."},
    {"topic": "strings",
     "code": "print('Hello World'.replace('World', 'Python'))",
     "explain": "replace(old, new) swaps all occurrences."},
    {"topic": "strings",
     "code": "print('a-b-c'.split('-'))",
     "explain": "split(sep) splits on the separator into a list."},
    {"topic": "strings",
     "code": "print('Hello'.find('l'))",
     "explain": "find() returns the index of the FIRST match."},

    # ---- ternary / range ----
    {"topic": "ternary",
     "code": "print('even' if 4 % 2 == 0 else 'odd')",
     "explain": "Ternary: value-if-true if condition else value-if-false."},
    {"topic": "ternary",
     "code": "print(list(range(1, 10, 2)))",
     "explain": "range(start, stop, step): start=1, stop=10 excluded, step=2."},
    {"topic": "ternary",
     "code": "print(list(range(10)))",
     "explain": "range(10) means 0 up to (but not including) 10."},

    # ---- loops ----
    {"topic": "loops",
     "code": "total = 0\nfor i in range(4):\n    total += i\nprint(total)",
     "explain": "Adds 0+1+2+3 = 6."},
    {"topic": "loops",
     "code": "i = 0\nwhile i < 3:\n    i += 1\nprint(i)",
     "explain": "The loop stops when i reaches 3."},

    # ---- collections ----
    {"topic": "collections",
     "code": "print([1, 2, 3].pop())",
     "explain": "pop() removes and returns the LAST item."},
    {"topic": "collections",
     "code": "nums = [1, 2]\nnums.append([3, 4])\nprint(nums)",
     "explain": "append adds the whole [3, 4] as ONE element."},
    {"topic": "collections",
     "code": "nums = [1, 2]\nnums.extend([3, 4])\nprint(nums)",
     "explain": "extend adds each element separately."},
    {"topic": "collections",
     "code": "print(len([1, 2, 3, 'a', True]))",
     "explain": "len() counts the number of items."},
    {"topic": "collections",
     "code": "d = {'a': 1, 'b': 2}\nprint(list(d.keys()))",
     "explain": "keys() gives the keys; list() turns the view into a list."},
    {"topic": "collections",
     "code": "d = {'a': 1, 'b': 2}\nprint(list(d.items()))",
     "explain": "items() yields (key, value) tuples."},

    # ---- sets ----
    {"topic": "sets",
     "code": "print({1, 2, 2, 3, 3, 3})",
     "explain": "Sets keep only unique values - duplicates disappear."},
    {"topic": "sets",
     "code": "print({1, 2, 3} & {2, 3, 4})",
     "explain": "& is the set intersection (items in both)."},

    # ---- identity / copying ----
    {"topic": "copying",
     "code": "x = [1, 2]\ny = x\nprint(x is y)",
     "explain": "y = x shares the SAME object, so identity is True."},
    {"topic": "copying",
     "code": "x = [1, 2]\ny = [1, 2]\nprint(x == y)",
     "explain": "== compares VALUES: both lists hold [1, 2]."},
    {"topic": "copying",
     "code": "x = [1, 2]\ny = [1, 2]\nprint(x is y)",
     "explain": "is compares IDENTITY: two separately-created lists are different objects."},
    {"topic": "copying",
     "code": "a = [[1, 2], [3, 4]]\nb = a.copy()\nb[0].append(9)\nprint(a)",
     "explain": "copy() is shallow - the inner lists are SHARED, so a[0] changes too."},

    # ---- functions / lambda ----
    {"topic": "functions",
     "code": "def add(a=1, b=2):\n    return a + b\nprint(add())",
     "explain": "Both defaults are used: 1 + 2 = 3."},
    {"topic": "functions",
     "code": "def add(*nums):\n    return sum(nums)\nprint(add(2, 4, 6, 8, 10, 12))",
     "explain": "*args packs all positional args into a tuple; sum() adds them."},
    {"topic": "lambda",
     "code": "print((lambda a, b: a + b)(3, 4))",
     "explain": "A nameless function called immediately with (3, 4)."},
    {"topic": "lambda",
     "code": "print(list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])))",
     "explain": "filter keeps only items where the lambda is True (evens)."},
    {"topic": "lambda",
     "code": "print(list(map(lambda n: n * 2, [1, 2, 3])))",
     "explain": "map transforms EVERY item (here, doubles each)."},

    # ---- comprehensions ----
    {"topic": "comprehensions",
     "code": "print([i ** 2 for i in range(5)])",
     "explain": "Squares of 0, 1, 2, 3, 4."},
    {"topic": "comprehensions",
     "code": "print([n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0])",
     "explain": "Comprehension with a condition keeps only the evens."},
    {"topic": "comprehensions",
     "code": "print({x % 3 for x in range(6)})",
     "explain": "A set comprehension - and sets keep unique results."},

    # ---- built-ins ----
    {"topic": "builtins",
     "code": "print(any([False, True]))",
     "explain": "any() is True if at least one item is truthy."},
    {"topic": "builtins",
     "code": "print(all([1, 2, 3]))",
     "explain": "all() is True only if EVERY item is truthy."},
    {"topic": "builtins",
     "code": "print(list(zip([1, 2], ['a', 'b'])))",
     "explain": "zip pairs up items position by position into tuples."},
    {"topic": "builtins",
     "code": "print(sorted([5, 2, 9, 1, 7]))",
     "explain": "sorted() returns a NEW list in ascending order."},
]

# --- helpers -------------------------------------------------------

def normalize(text):
    """Make two answers comparable: lowercase, no quotes, no spaces."""
    return "".join(str(text).strip().strip("'\"").split()).lower()


def run_snippet(code):
    """Execute the snippet and capture everything it prints."""
    buffer = io.StringIO()
    namespace = {}
    with contextlib.redirect_stdout(buffer):
        exec(code, namespace)
    return buffer.getvalue().strip()


def read_input(prompt):
    try:
        value = input(prompt)
    except EOFError:
        return None
    if value.strip().lower() in ("q", "quit"):
        return "QUIT"
    return value


def pick_topic():
    topics = sorted({s["topic"] for s in SNIPPETS})
    print("\nTopics:")
    for i, t in enumerate(topics, 1):
        print(f"  {i:>2}. {t}")
    print("   0. ALL topics")
    while True:
        value = read_input("\nPick a topic (number): ")
        if value == "QUIT" or value is None:
            return None
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


def pick_count(total):
    prompt = f"How many snippets? (Enter for all {total}): "
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


def show_code(code):
    print("  Code to predict:")
    print("  " + "-" * 40)
    for line in code.splitlines():
        print("  " + line)
    print("  " + "-" * 40)


def run_pass(pool):
    correct = 0
    wrong = []
    for i, s in enumerate(pool, 1):
        print(f"\n----------------------------------------")
        print(f"Snippet {i} / {len(pool)}  [{s['topic']}]")
        show_code(s["code"])
        actual = run_snippet(s["code"])
        user = read_input("  Predicted output: ")
        if user == "QUIT" or user is None:
            return correct, wrong, True

        is_right = normalize(user) == normalize(actual)
        mark = "CORRECT" if is_right else "WRONG"
        print(f"\n  [{mark}]")
        print(f"  You said:    {user}")
        print(f"  Actual:      {actual}")
        if not is_right:
            print(f"  Why: {s['explain']}")
            wrong.append(s)
        else:
            print(f"  Why: {s['explain']}")

        if is_right:
            correct += 1

    return correct, wrong, False


def main():
    print("============================================")
    print(" PREDICT-RUN TRAINER")
    print(" Rule: predict the output BEFORE running.")
    print(" Enter 'q' anytime to quit")
    print("============================================")

    topic = pick_topic()
    if topic == "QUIT":
        return
    pool = SNIPPETS if topic is None else [s for s in SNIPPETS if s["topic"] == topic]

    count = pick_count(len(pool))
    if count is None:
        return

    random.shuffle(pool)
    pool = pool[:count]

    correct, wrong, quit_now = run_pass(pool)
    total = len(pool)
    print("\n============================================")
    print(f" SCORE: {correct} / {total}")
    if total:
        print(f" ({round(100 * correct / total)}%)")
    print("============================================")

    if wrong and not quit_now:
        print(f"\nYou missed {len(wrong)}. Practicing those again...")
        random.shuffle(wrong)
        correct2, _, _ = run_pass(wrong)
        print(f"\nSecond round: {correct2} / {len(wrong)} correct.")
        print("Keep the ones you still missed in mind and retry tomorrow.")

    print("\nTip: the wrong ones are what you actually need to study.")


if __name__ == "__main__":
    main()
