from collections import deque

dq = deque([1, 2, 3])         # O(n) to create from iterable

dq.append(4)                  # O(1)  → add to right
dq.appendleft(0)               # O(1)  → add to left
dq.extend([5, 6])              # O(k)  → extend right with k elements
dq.extendleft([-1, -2])        # O(k)  → extend left with k elements (in reverse order)
dq.pop()                       # O(1)  → remove from right
dq.popleft()                   # O(1)  → remove from left
dq.remove(3)                   # O(n)  → remove first occurrence (search needed)
dq.rotate(2)                   # O(1) if k is small, O(n) if k is large
dq.clear()                     # O(1)  → remove all elements


