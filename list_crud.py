# ============================================
# CRUD ON LISTS
# C - Create, R - Read, U - Update, D - Delete
# ============================================

lst = [1, 2, 3, 'a', True]
print("Original:", lst)

print("\n=== C - CREATE (append, extend, insert) ===")
# append - adds ONE item (the whole argument becomes one element)
lst.append([1, 2])
print("after append([1, 2]):", lst)
# [1, 2, 3, 'a', True, [1, 2]]

# extend - adds each element of the iterable separately
lst = [1, 2, 3, 'a', True]           # reset
lst.extend([1, 2])
print("after extend([1, 2]):", lst)
# [1, 2, 3, 'a', True, 1, 2]

# insert - insert at index (shifts the rest)
lst = [1, 2, 3, 'a', True]           # reset
lst.insert(3, 'Hi')
print("after insert(3, 'Hi'):", lst)
# [1, 2, 3, 'Hi', 'a', True]

print("\n=== R - READ ===")
print("lst[0]:", lst[0])
print("lst[-1]:", lst[-1])

print("\n=== U - UPDATE ===")
lst[-1] = False
print("after lst[-1] = False:", lst)

print("\n=== D - DELETE (pop, del) ===")
# pop - deletes an item and RETURNS it
lst = [1, 2, 3, 'a', True]           # reset
removed = lst.pop()                  # deletes last item, returns it
print("pop() returned:", removed, "| list now:", lst)

lst = [1, 2, 3, 'a', True]           # reset
removed = lst.pop(-3)                # pop by negative index
print("pop(-3) returned:", removed, "| list now:", lst)

# del - removes item at index, does NOT return it
lst = [1, 2, 'a']                    # reset
del lst[0]
print("after del lst[0]:", lst)

print("\n=== 8. Combined example ===")
lst = [1, 2, 'a']
x = lst.pop(-3)                      # pops index -3 (value 1), lst = [2, 'a']
lst[1] = lst[1] * x                  # 'a' * 1 = 'aa'
print("lst[1] = lst[1] * x ->", lst)  # [2, 'aa']
print("len(lst):", len(lst))
