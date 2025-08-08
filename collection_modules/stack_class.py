from collections import deque

'''
Python does not have a dedicated stack data type like Java’s Stack.
The recommended way to implement a stack is by using:
collections.deque → Fast push and pop from both ends (O(1) time).
list → Works for stack (push with append, pop with pop()), but popping from the front is slow.

'''

stack = deque([1, 2, 3])   # O(n) → create stack from iterable

stack.append(4)            # O(1) → push (add to top)
stack.append(5)            # O(1) → push (add to top)
stack.pop()                # O(1) → pop (remove from top)
top = stack[-1]             # O(1) → peek (view top element)
size = len(stack)           # O(1) → get size
is_empty = not stack        # O(1) → check if empty
stack.clear()               # O(1) → clear stack
found = (2 in stack)        # O(n) → search for element
for item in reversed(stack): # O(n) → iterate in LIFO order
    pass




# ========================== List as Stack ==========================


stack = [1, 2, 3]     # O(n) to create from iterable   # Create stack   
stack.append(4)       # O(1) amortized      # Push (add to top)     
stack.pop()           # O(1)     # Pop (remove from top)   
top = stack[-1]       # O(1)    # Peek (view top element)
size = len(stack)      # O(1)    # Get size
is_empty = not stack    # O(1)     # Check if empty
found = (2 in stack)    # O(n) # Search for element
for item in reversed(stack):  # O(n) # Iterate in LIFO order
    pass
stack.clear()            # O(1) # Clear stack
