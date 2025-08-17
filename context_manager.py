"""
Context Manager in Python

A **context manager** in Python is an object that properly manages resources by setting things up before a block of code runs and cleaning them up afterward — even if an error occurs.

The most common way you’ve seen it is with the `with` statement.

Why we need it?
Some resources (like files, database connections, locks, sockets) need to be released properly after use. Without proper cleanup, you may get memory leaks, file locks, or unexpected errors.
"""

# Example 1: File handling without context manager
f = open("data.txt", "w+")
try:
    content = f.read()
finally:
    f.close()  # you must remember to close the file

"""
This works, but it’s verbose.
"""

# Example 2: Using a context manager (with statement)
with open("data.txt", "r") as f:
    content = f.read()
# file automatically closed here

"""
Here, Python automatically calls:
- f.__enter__() when entering the block
- f.__exit__() when leaving the block (even if an exception happens)
"""

# Example 3: Creating Your Own Context Manager using a class
class MyContext:
    def __enter__(self):
        print("Entering...")
        return "Resource"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting... Cleaning up")

with MyContext() as r:
    print("Using:", r)

"""
Output:
Entering...
Using: Resource
Exiting... Cleaning up
"""

# Example 4: Creating a Context Manager using contextlib
from contextlib import contextmanager

@contextmanager
def my_manager():
    print("Setup")
    yield "Resource"
    print("Cleanup")

with my_manager() as r:
    print("Using:", r)

"""
✅ In short:  
A context manager is Python’s way to automate setup and cleanup of resources using the `with` statement.
"""
