# Python list operations with time complexity

lst = [1, 2, 3]

lst.append(4)          # O(1)*  - append at end (amortized)
lst.insert(0, 0)       # O(n)   - insert at start (shift elements)
lst.extend([5, 6])     # O(k)   - extend with iterable of length k
lst.pop()              # O(1)   - remove from end
lst.pop(0)             # O(n)   - remove from start (shift elements)
lst.remove(3)          # O(n)   - remove first occurrence by value
lst[1] = 10            # O(1)   - index assignment
x = lst[1]             # O(1)   - index access
len(lst)               # O(1)   - length of list
y = 5 in lst           # O(n)   - search element
count_5 = lst.count(5) # O(n)   - count occurrences
index_5 = lst.index(5) # O(n)   - find index of first occurrence
lst.sort()             # O(n log n) - sort in place
sorted_lst = sorted(lst) # O(n log n) - return sorted copy
lst.reverse()          # O(n)   - reverse in place
rev_iter = reversed(lst) # O(1) - reversed iterator
lst.clear()            # O(1)   - clear list
