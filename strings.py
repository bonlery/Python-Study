# ============================================
# COMPREHENSIVE PYTHON STRINGS GUIDE
# ============================================

# --------------------------------------------
# 1. CREATION & BASICS
# --------------------------------------------

# --- Basic string creation ---
single = 'hello'               # single quotes
double = "world"               # double quotes
triple = '''multi
line'''                        # triple quotes (can span lines)
triple2 = """also
multi line"""                  # triple double quotes

print("=== 1.1 Basic Creation ===")
print(single, double)          # hello world
print(repr(triple))            # 'multi\nline'
print(repr(triple2))           # 'also\nmulti line'

# --- Raw strings (ignore escape characters) ---
print("\n=== 1.2 Raw Strings ===")
normal = "path\new\file"       # \e is not a real escape, treated as literal 'e'
raw = r"path\new\file"         # backslashes preserved as-is
print(normal)                  # path\new\file
print(raw)                     # path\new\file

# --- Byte strings ---
print("\n=== 1.3 Byte Strings ===")
b = b"hello"                   # bytes object
print(type(b))                 # <class 'bytes'>
print(b)                       # b'hello'
print(b[0])                    # 104 (integer, not 'h')

# --- String from other types ---
print("\n=== 1.4 String Conversion ===")
print(str(42))                 # '42'
print(str(3.14))               # '3.14'
print(str(True))               # 'True'
print(str([1, 2, 3]))          # '[1, 2, 3]'
print(str(None))               # 'None'

# --- ord() and chr() ---
print("\n=== 1.5 ord() and chr() ===")
print(ord('A'))                # 65
print(ord('a'))                # 97
print(chr(65))                 # 'A'
print(chr(97))                 # 'a'
print(chr(8364))               # '€' (Euro sign)

# --- String repetition and concatenation ---
print("\n=== 1.6 Repetition & Concatenation ===")
print("ha" * 3)                # 'hahaha'
print("hello" + " " + "world") # 'hello world'

# --- Immutability ---
print("\n=== 1.7 Immutability ===")
s = "hello"
# s[0] = 'H'                  # TypeError: 'str' object does not support item assignment
s2 = "H" + s[1:]               # must create a new string
print(s2)                      # 'Hello'

# --- Sequence behavior ---
print("\n=== 1.8 Sequence Behavior ===")
s = "Python"
print(len(s))                  # 6
print("P" in s)                # True
print("xyz" in s)              # False
print(list(s))                 # ['P', 'y', 't', 'h', 'o', 'n']
for ch in s:
    print(ch, end=" ")         # P y t h o n
print()

# --- Escape characters ---
print("\n=== 1.9 Escape Characters ===")
print("line1\nline2")          # line1
                              # line2
print("a\tb")                  # a	b
print("quote: \"hello\"")      # quote: "hello"
print("back\\slash")           # back\slash
print("\0null")                # null (empty char before 'null')
print("cr\return")             # carriage return overwrites
print("\x41")                  # A (hex)
print("\u0041")                # A (unicode 4-digit)
import sys; sys.stdout.reconfigure(encoding="utf-8")
print("\U0001F600")              # 😀 (unicode codepoint, U+1F600)
print("\101")                  # A (octal)


# --------------------------------------------
# 2. INDEXING & SLICING
# --------------------------------------------

print("\n=== 2. Indexing & Slicing ===")
s = "Python"
print("s:", s)                 # 'Python'

# Indexing
print("s[0]:", s[0])          # 'P'
print("s[-1]:", s[-1])        # 'n'
print("s[5]:", s[5])          # 'n'

# Slicing [start:stop:step]
print("s[1:4]:", s[1:4])      # 'yth'
print("s[:3]:", s[:3])        # 'Pyt'
print("s[3:]:", s[3:])        # 'hon'
print("s[::2]:", s[::2])      # 'Pto' (every 2nd char)
print("s[::-1]:", s[::-1])    # 'nohtyP' (reverse)
print("s[1:5:2]:", s[1:5:2])  # 'yh' (step of 2)
print("s[-3:]:", s[-3:])      # 'hon'
print("s[:-2]:", s[:-2])      # 'Pyth'


# --------------------------------------------
# 3. ALL STRING METHODS
# --------------------------------------------

print("\n=== 3.1 Case Methods ===")
s = "Hello World"
print(s.upper())               # 'HELLO WORLD'
print(s.lower())               # 'hello world'
print(s.title())               # 'Hello World'
print(s.capitalize())          # 'Hello world'
print(s.swapcase())            # 'hELLO wORLD'
print("HELLO".casefold())      # 'hello' (more aggressive lowercasing)
print("ß".casefold())          # 'ss'
print("STRASSE".casefold())    # 'strasse'


print("\n=== 3.2 Search & Find Methods ===")
text = "Hello World, Hello Python"

# find / rfind
print(text.find("Hello"))      # 0
print(text.find("Hello", 1))   # 13 (start searching from index 1)
print(text.rfind("Hello"))     # 13 (rightmost)
print(text.find("Java"))       # -1 (not found)

# index / rindex (same as find but raises ValueError if not found)
print(text.index("Hello"))     # 0
print(text.rindex("Hello"))    # 13
# text.index("Java")           # ValueError: substring not found

# count
print(text.count("Hello"))     # 2
print(text.count("l"))         # 4
print(text.count("Hello", 0, 13))  # 1 (only in first 13 chars)

# startswith / endswith
print(text.startswith("Hello"))     # True
print(text.startswith("World", 6))  # True (check at index 6)
print(text.endswith("Python"))      # True
print(text.endswith(("World", "Python")))  # True (tuple of suffixes)
print(text.startswith(("Hello", "Hi")))    # True (tuple of prefixes)


print("\n=== 3.3 Transformation Methods ===")
s = "  Hello World  "

# strip / lstrip / rstrip
print(s.strip())               # 'Hello World'
print(s.lstrip())              # 'Hello World  '
print(s.rstrip())              # '  Hello World'
print("***hello***".strip("*"))    # 'hello'
print("***hello***".lstrip("*"))   # 'hello***'
print("***hello***".rstrip("*"))   # '***hello'
print("xyhelloyx".strip("xy"))     # 'hello' (strips any char in the set)

# removeprefix / removesuffix (Python 3.9+)
print("HelloWorld".removeprefix("Hello"))   # 'World'
print("HelloWorld".removesuffix("World"))   # 'Hello'
print("TestHello".removeprefix("World"))    # 'TestHello' (no change)
print("TestHello".removesuffix("World"))    # 'TestHello' (no change)

# replace
print("hello world".replace("world", "python"))     # 'hello python'
print("aaa".replace("a", "b", 2))                   # 'bba' (replace only 2)

# center / ljust / rjust / zfill
print("hello".center(20, "-"))   # '-------hello--------'
print("hello".ljust(20, "."))    # 'hello...............'
print("hello".rjust(20, "."))    # '...............hello'
print("42".zfill(5))             # '00042'
print("-42".zfill(5))            # '-0042'
print("hello".center(20))        # '       hello        ' (spaces default)

# expandtabs
print("a\tb".expandtabs(4))      # 'a   b'
print("a\tb".expandtabs(12))     # 'a           b'
print("one\ttwo\tthree".expandtabs(8))  # 'one     two     three'

# translate / maketrans
table = str.maketrans("aeiou", "12345")  # map vowels to numbers
print("hello world".translate(table))    # 'h2ll4 w4rld'

table2 = str.maketrans({"a": "A", "e": "E", "i": None})  # None = delete
print("africa".translate(table2))        # 'Afr_ca' (i removed)

table3 = str.maketrans("abc", "ABC", "xyz")  # 3 args: from, to, delete
print("abcxyz".translate(table3))        # 'ABC'


print("\n=== 3.4 Split & Join Methods ===")

# split / rsplit
print("a,b,c".split(","))           # ['a', 'b', 'c']
print("a,b,c".split(",", 1))        # ['a', 'b,c'] (maxsplit=1)
print("a,b,c".rsplit(",", 1))       # ['a,b', 'c'] (split from right)
print("  a  b  c  ".split())        # ['a', 'b', 'c'] (whitespace, strips)
print("a b  c   d".split(" "))      # ['a', 'b', '', 'c', '', '', 'd']
print("one,,two,,three".split(",")) # ['one', '', 'two', '', 'three']

# splitlines
print("line1\nline2\nline3".splitlines())       # ['line1', 'line2', 'line3']
print("line1\r\nline2".splitlines())            # ['line1', 'line2']
print("line1\nline2".splitlines(True))          # ['line1\n', 'line2\n'] (keepends)

# partition / rpartition
print("hello-world-test".partition("-"))        # ('hello', '-', 'world-test')
print("hello-world-test".rpartition("-"))       # ('hello-world', '-', 'test')
print("hello-world-test".partition("+"))        # ('hello-world-test', '', '')

# join
print(",".join(["a", "b", "c"]))               # 'a,b,c'
print(" ".join(["Hello", "World"]))             # 'Hello World'
print("\n".join(["line1", "line2"]))            # 'line1\nline2'
print("".join(["h", "e", "l", "l", "o"]))      # 'hello'


print("\n=== 3.5 Type Checking Methods ===")
# isalpha / isdigit / isalnum
print("hello".isalpha())         # True
print("hello123".isalpha())      # False
print("123".isdigit())           # True
print("123a".isdigit())          # False
print("hello123".isalnum())      # True
print("hello 123".isalnum())     # False (space)

# isnumeric / isdecimal
print("123".isnumeric())         # True
print("123".isdecimal())         # True
print("½".isnumeric())           # True
print("½".isdecimal())           # False
print("²".isnumeric())           # True (superscript 2)
print("²".isdecimal())           # False

# isidentifier / keyword check
print("my_var".isidentifier())   # True
print("123var".isidentifier())   # False
print("_private".isidentifier()) # True
import keyword
print(keyword.iskeyword("if"))   # True
print(keyword.iskeyword("my_var"))  # False

# isupper / islower / istitle / isspace
print("HELLO".isupper())         # True
print("hello".islower())         # True
print("Hello World".istitle())   # True
print("   ".isspace())           # True
print("\t\n ".isspace())         # True

# isprintable / isascii
print("hello".isprintable())     # True
print("hello\n".isprintable())   # False
print("hello".isascii())         # True
print("cafe\u0301".isascii())    # False (accented character)


# --------------------------------------------
# 4. STRING FORMATTING
# --------------------------------------------

print("\n=== 4.1 %-Formatting (old style) ===")
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))       # 'Name: Alice, Age: 30'
print("Pi: %.2f" % 3.14159)                     # 'Pi: 3.14'
print("Padded: %10s" % "hi")                    # '        hi'
print("Left: %-10s." % "hi")                    # 'hi        .'
print("Hex: %x, Oct: %o" % (255, 255))  # 'Hex: ff, Oct: 377'

print("\n=== 4.2 str.format() ===")
print("Name: {}, Age: {}".format("Bob", 25))              # 'Name: Bob, Age: 25'
print("{0} is {1}, {0} is cool".format("Python", "great"))  # 'Python is great, Python is cool'
print("{name} is {age}".format(name="Charlie", age=35))    # 'Charlie is 35'

# Format spec
print("{:.2f}".format(3.14159))         # '3.14'
print("{:>10}".format("hi"))            # '        hi'
print("{:<10}".format("hi"))            # 'hi        '
print("{:^10}".format("hi"))            # '    hi    '
print("{:0>5}".format(42))              # '00042'
print("{:,}".format(1000000))           # '1,000,000'
print("{:.2%}".format(0.756))           # '75.60%'
print("{:x}".format(255))               # 'ff'
print("{:#x}".format(255))              # '0xff'

# Nested access
person = {"name": "Dave", "scores": [90, 85, 92]}
print("{0[name]} scores: {0[scores][0]}".format(person))  # 'Dave scores: 90'

print("\n=== 4.3 f-Strings (formatted string literals) ===")
name = "Eve"
age = 28
print(f"Name: {name}, Age: {age}")           # 'Name: Eve, Age: 28'
print(f"Next year: {age + 1}")               # 'Next year: 29'
print(f"Pi: {3.14159:.2f}")                  # 'Pi: 3.14'

# Format spec in f-strings
print(f"{'hello':>10}")                       # '     hello'
print(f"{'hello':<10}.")                      # 'hello     .'
print(f"{'hello':^10}")                       # '   hello   '
print(f"{1000000:,}")                         # '1,000,000'
print(f"{0.756:.2%}")                         # '75.60%'
print(f"{255:#x}")                            # '0xff'

# Debugging with = (Python 3.8+)
x = 42
print(f"{x = }")                              # 'x = 42'
print(f"{x + 1 = }")                          # 'x + 1 = 43'
print(f"{x = :.2f}")                          # 'x = 42.00'

# Expressions in f-strings
items = ["a", "b", "c"]
print(f"Items: {', '.join(items)}")           # 'Items: a, b, c'
print(f"2 + 2 = {2 + 2}")                    # '2 + 2 = 4'

# Multiline f-strings
name = "Frank"
age = 40
info = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Doubled: {age * 2}"
)
print(info)

print("\n=== 4.4 string.Template ===")
from string import Template
t = Template("Hello, $name! You are $age.")
print(t.substitute(name="Grace", age=33))     # 'Hello, Grace! You are 33.'
print(t.safe_substitute(name="Hank"))          # 'Hello, Hank! You are $age.' (missing = left)


# --------------------------------------------
# 5. ENCODING & COMPARISON
# --------------------------------------------

print("\n=== 5.1 Encoding & Decoding ===")
s = "café"
encoded = s.encode("utf-8")
print(encoded)                   # b'caf\xc3\xa9'
print(type(encoded))             # <class 'bytes'>
print(len(s))                    # 4
print(len(encoded))              # 5 (é is 2 bytes in UTF-8)

decoded = encoded.decode("utf-8")
print(decoded)                   # 'café'

# ASCII encoding (fails on non-ASCII)
ascii_bytes = "hello".encode("ascii")
print(ascii_bytes)               # b'hello'

# Latin-1 encoding
latin_bytes = "café".encode("latin-1")
print(latin_bytes)               # b'caf\xe9'

# Encoding errors
print("café".encode("ascii", errors="replace"))  # b'caf?'
print("café".encode("ascii", errors="ignore"))   # b'caf'
print("café".encode("ascii", errors="xmlcharrefreplace"))  # b'caf&#233;'

# Byte strings
b = b"hello"
print(b[0])                      # 104 (ASCII code)
print(chr(b[0]))                 # 'h'
print(bytes([72, 101, 108, 108, 111]))  # b'Hello'

print("\n=== 5.2 String Comparison ===")
print("apple" == "apple")        # True
print("apple" == "Apple")        # False
print("apple" < "banana")        # True (lexicographic)
print("abc" < "abd")             # True
print("abc" > "ab")              # True

# Case-insensitive comparison
print("Hello".lower() == "hello".lower())  # True
print("Hello".casefold() == "hello".casefold())  # True

# casefold is more aggressive than lower for certain languages
print("Straße".casefold() == "strasse".casefold())  # True


# --------------------------------------------
# 6. REGULAR EXPRESSIONS
# --------------------------------------------

import re

print("\n=== 6.1 re.search & re.match ===")
text = "The price is 42 dollars"

# search: find first match anywhere in string
m = re.search(r"\d+", text)
print(m.group())                 # '42'
print(m.span())                  # (14, 16)

# match: only matches at the beginning
m2 = re.match(r"The", text)
print(m2.group())                # 'The'
m3 = re.match(r"\d+", text)
print(m3)                        # None (no match at start)

print("\n=== 6.2 re.findall & re.finditer ===")
text = "cat bat rat fat"
print(re.findall(r"[cbrf]at", text))  # ['cat', 'bat', 'rat', 'fat']
print(re.findall(r"\d+", "12 abc 34 def 56"))  # ['12', '34', '56']

# finditer gives match objects with positions
for m in re.finditer(r"\d+", "12 abc 34"):
    print(f"  {m.group()} at {m.span()}", end="")
print()

print("\n=== 6.3 re.sub & re.split ===")
print(re.sub(r"\d+", "NUM", "a1 b2 c3"))  # 'aNUM bNUM cNUM'
print(re.sub(r"(\w+)", r"\1!", "hi there"))  # 'hi! there!'
print(re.subn(r"\d+", "X", "a1 b2 c3"))     # ('aX bX cX', 3) (tuple with count)

print(re.split(r"\s+", "one  two   three"))  # ['one', 'two', 'three']
print(re.split(r"[,\s]+", "a, b ,c,  d"))    # ['a', 'b', 'c', 'd']

print("\n=== 6.4 Common Patterns ===")
# Email
email = "user@example.com"
print(bool(re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", email)))  # True

# Phone (simple US format)
phone = "(555) 123-4567"
print(bool(re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone)))    # True

# Date (YYYY-MM-DD)
date = "2026-01-15"
print(bool(re.match(r"^\d{4}-\d{2}-\d{2}$", date)))          # True

# Password: min 8 chars, uppercase, lowercase, digit
print(bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", "Str0ngPass")))  # True
print(bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", "weak")))         # False

# Groups
m = re.match(r"(\w+)@(\w+)\.(\w+)", "user@example.com")
if m:
    print(m.group(0))           # 'user@example.com' (full match)
    print(m.group(1))           # 'user'
    print(m.group(2))           # 'example'
    print(m.group(3))           # 'com'
    print(m.groups())           # ('user', 'example', 'com')

# Named groups
m2 = re.match(r"(?P<user>\w+)@(?P<domain>\w+)\.(\w+)", "test@site.org")
if m2:
    print(m2.group("user"))     # 'test'
    print(m2.group("domain"))   # 'site'

# Compiled pattern (reusable, slightly faster)
pattern = re.compile(r"\b\w{4}\b")
print(pattern.findall("hi there test four five"))  # ['test', 'five']


# --------------------------------------------
# 7. STRING MODULE & ADVANCED
# --------------------------------------------

import string

print("\n=== 7.1 string Module Constants ===")
print("ascii_letters:", string.ascii_letters)      # 'abcdef...XYZ'
print("ascii_lowercase:", string.ascii_lowercase)   # 'abcdef...xyz'
print("ascii_uppercase:", string.ascii_uppercase)   # 'ABCDEF...XYZ'
print("digits:", string.digits)                     # '0123456789'
print("octdigits:", string.octdigits)               # '01234567'
print("hexdigits:", string.hexdigits)               # '0123456789abcdefABCDEF'
print("punctuation:", string.punctuation)           # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print("whitespace:", repr(string.whitespace))       # ' \t\n\r\x0b\x0c'
print("printable:", string.printable)               # digits + ascii_letters + punctuation + whitespace

print("\n=== 7.2 textwrap Module ===")
import textwrap

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# wrap: break into lines
wrapped = textwrap.wrap(lorem, width=40)
for line in wrapped:
    print(f"  |{line}|")

# fill: wrap and join into single string
filled = textwrap.fill(lorem, width=40)
print(filled)

# indent
indented = textwrap.indent(filled, "  > ")
print(indented)

# dedent
dedented = textwrap.dedent(indented)
print(dedented)

# shorten
shortened = textwrap.shorten(lorem, width=30, placeholder="...")
print(shortened)                     # 'Lorem ipsum dolor sit amet,...'

print("\n=== 7.3 Common String Patterns ===")

# Palindrome check
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))      # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))        # False

# Reverse a string
s = "Hello"
print(s[::-1])                       # 'olleH'

# Count vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

print(count_vowels("Hello World"))   # 3

# Caesar cipher (shift letters)
def caesar(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return "".join(result)

print(caesar("Hello World", 3))      # 'Khoor Zruog'
print(caesar("Khoor Zruog", -3))     # 'Hello World'

# Word frequency
def word_freq(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_freq("the cat sat on the mat the cat"))  # {'the': 3, 'cat': 2, ...}

# String to binary
def to_binary(s):
    return " ".join(format(ord(c), "08b") for c in s)

print(to_binary("Hi"))               # '01001000 01101001'

# Binary to string
def from_binary(b):
    return "".join(chr(int(x, 2)) for x in b.split())

print(from_binary("01001000 01101001"))  # 'Hi'

# Remove duplicates preserving order
def remove_dupes(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)

print(remove_dupes("hello world"))   # 'helo wrd'

# Isogram check (no repeating letters)
def is_isogram(s):
    letters = [c.lower() for c in s if c.isalpha()]
    return len(letters) == len(set(letters))

print(is_isogram("lumberjacks"))     # True
print(is_isogram("hello"))           # False
