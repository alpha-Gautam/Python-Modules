from collections import Counter

# Initialization
c1 = Counter('banana')
c2 = Counter({'a': 2, 'b': 1})
c3 = Counter(a=3, b=2)

print("c1 Counter from string:", c1)
print("c2 Counter from dict:", c2)
print("c3 Counter from kwargs:", c3)

# Accessing counts
print("c1 Count of 'a' in c1:", c1['a'])
print("c1 Count of 'z' in c1 (missing key):", c1['z'])  # returns 0

# elements()
print("c2 Elements in c2:", list(c2.elements()))

# values()
print("c1 Values in c1:", list(c1.values()))
print("c2 Values in c2:", list(c2.values()))
print("c3 Values in c3:", list(c3.values()))

# most_common()
print("c1 Most common 2 in c1:", c1.most_common(2))

# update()
c1.update('apple')
print("c1 After update with 'apple':", c1)

# subtract()
c1.subtract('banana')
print("c1 After subtracting 'banana':", c1)

# Arithmetic operations
c4 = Counter('abbb')
c5 = Counter('bcc')

print("c4:", c4)
print("c5:", c5)
print("Addition (c4 + c5):", c4 + c5)
print("Subtraction (c4 - c5):", c4 - c5)
print("Intersection (c4 & c5):", c4 & c5)
print("Union (c4 | c5):", c4 | c5)

# clear()
c6 = Counter('hello')
c6.clear()
print("c6 After clear():", c6)

# copy()
c7 = Counter('hello')
c8 = c7.copy()
print("c8 Copy of c7:", c8)

# Convert to dict
print("c7 Dict version of c7:", dict(c7))

# total() - Python 3.10+
if hasattr(c7, 'total'):
    print("c7 Total count in c7:", c7.total())
else:
    print("c7 Manual total count in c7:", sum(c7.values()))
