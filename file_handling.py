# ============================================
# FILE HANDLING
# ============================================

FILENAME = "sample_output.txt"

print("=== 1. open() with write mode 'w' ===")
# 'w' - write (overwrites the file if it exists)
f = open(FILENAME, "w")
f.write("Line 1\n")
f.write("Line 2\n")
f.close()                              # always close the file
print("wrote 2 lines with open()/write()/close()")

print("\n=== 2. with open() - auto-closes ===")
with open(FILENAME, "w") as f:
    f.write("Hello\n")
    f.writelines(["world\n", "Python\n"])
# no need to call close() - 'with' handles it
print("wrote with 'with open()'")

print("\n=== 3. File modes ===")
# 'r'  - read (default, error if file missing)
# 'w'  - write (overwrite or create)
# 'a'  - append (add to the end)
# 'x'  - exclusive create (error if file already exists)
print("r = read, w = write, a = append, x = exclusive create")

print("\n=== 4. read, readline, readlines ===")
with open(FILENAME, "r") as f:
    content = f.read()
    print("read():", repr(content))

with open(FILENAME, "r") as f:
    first = f.readline()
    print("readline():", repr(first))

with open(FILENAME, "r") as f:
    lines = f.readlines()
    print("readlines():", lines)

print("\n=== 5. Appending with 'a' ===")
with open(FILENAME, "a") as f:
    f.write("Appended line\n")
with open(FILENAME, "r") as f:
    print("file after append:", repr(f.read()))

print("\n=== 6. Exclusive create with 'x' ===")
try:
    with open("new_exclusive.txt", "x") as f:
        f.write("just created\n")
    print("created new_exclusive.txt")
except FileExistsError:
    print("FileExistsError: file already exists")

print("\n=== 7. Handling a missing file ===")
try:
    with open("does_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("FileNotFoundError: no such file - caught safely")

print("\n=== 8. Proper file closing (check closed) ===")
f = open(FILENAME, "r")
print("is closed before close():", f.closed)
f.close()
print("is closed after close():", f.closed)
