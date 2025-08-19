"""
Python Built-in Data Structures: Internal Implementation and Behind-the-Scenes Details

This module explains how Python's core data structures work internally,
including their time complexities, memory layouts, and algorithmic implementations.
"""

import time
import sys
import random
from collections import namedtuple

# ============================================================================
# DICTIONARY (dict) - Hash Table Implementation
# ============================================================================

"""
DICTIONARY INTERNALS:

1. HASH TABLE STRUCTURE:
   - Python dictionaries use an open addressing hash table with random probing
   - Since Python 3.7+, dictionaries maintain insertion order (ordered dict)
   - Uses a compact representation to save memory

2. HASH TABLE COMPONENTS:
   - Hash Function: Uses object's __hash__() method
   - Collision Resolution: Open addressing with random probing
   - Load Factor: Resizes when 2/3 full to maintain performance

3. MEMORY LAYOUT (Python 3.6+):
   Combined Table: [hash, key, value] entries stored sequentially
   Sparse Index: Array of indices pointing to the combined table
   
   Benefits:
   - 20-25% memory savings
   - Better cache locality
   - Preserves insertion order

4. OPERATIONS COMPLEXITY:
   - Average: O(1) for get, set, delete
   - Worst case: O(n) when many hash collisions occur
   - Space: O(n)
"""

def demonstrate_dict_internals():
    """Demonstrate dictionary internal behavior"""
    
    # Hash values and collision handling
    d = {}
    
    # Python uses hash() function for keys
    print("=== DICTIONARY HASH EXAMPLES ===")
    print(f"hash('hello'): {hash('hello')}")
    print(f"hash(42): {hash(42)}")
    print(f"hash((1, 2)): {hash((1, 2))}")
    
    # Dictionary resizing behavior
    d = {}
    print(f"\nInitial dict size: {d.__sizeof__()} bytes")
    
    # Add elements to see resizing
    for i in range(10):
        d[i] = i * 2
        if i in [0, 4, 8]:
            print(f"After {i+1} elements: {d.__sizeof__()} bytes")
    
    # Insertion order preservation (Python 3.7+)
    ordered_dict = {'c': 3, 'a': 1, 'b': 2}
    print(f"\nInsertion order preserved: {list(ordered_dict.keys())}")


# ============================================================================
# LIST - Dynamic Array Implementation
# ============================================================================

"""
LIST INTERNALS:

1. DYNAMIC ARRAY STRUCTURE:
   - Python lists are implemented as dynamic arrays (like C++ vector)
   - Contiguous memory allocation for better cache performance
   - Over-allocates memory to amortize the cost of resizing

2. MEMORY MANAGEMENT:
   - Growth Pattern: When full, allocates ~1.125x current size
   - Shrinking: Only shrinks when size drops significantly below capacity
   - Each element is a pointer to the actual Python object

3. OPERATIONS COMPLEXITY:
   - Access by index: O(1)
   - Append: O(1) amortized
   - Insert at beginning/middle: O(n)
   - Delete: O(n) for arbitrary position, O(1) for end
   - Search: O(n)

4. MEMORY LAYOUT:
   [PyListObject header][pointer1][pointer2][...][pointerN][unused slots]
"""

def demonstrate_list_internals():
    """Demonstrate list internal behavior"""
    
    print("\n=== LIST INTERNALS EXAMPLES ===")
    
    # Memory growth pattern
    import sys
    lst = []
    prev_size = 0
    
    print("List growth pattern:")
    for i in range(15):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != prev_size:
            print(f"Length {len(lst)}: {current_size} bytes (capacity increased)")
            prev_size = current_size
    
    # List operations performance
    import time
    
    # Append vs Insert at beginning
    test_list = list(range(10000))
    
    # Append (fast)
    start = time.time()
    test_list.append(10000)
    append_time = time.time() - start
    
    # Insert at beginning (slow)
    start = time.time()
    test_list.insert(0, -1)
    insert_time = time.time() - start
    
    print(f"\nAppend time: {append_time:.8f}s")
    print(f"Insert at beginning time: {insert_time:.8f}s")


# ============================================================================
# SET - Hash Table for Unique Elements
# ============================================================================

"""
SET INTERNALS:

1. HASH TABLE IMPLEMENTATION:
   - Similar to dictionary but stores only keys (no values)
   - Uses open addressing with random probing
   - Maintains uniqueness through hash-based lookups

2. OPERATIONS COMPLEXITY:
   - Add, Remove, Contains: O(1) average, O(n) worst case
   - Union, Intersection: O(min(len(s1), len(s2)))
   - Difference: O(len(s1))

3. MEMORY EFFICIENCY:
   - More memory efficient than dict for storing unique items
   - No value storage, only key hashes and references

4. SET OPERATIONS ALGORITHMS:
   - Union: Iterate through both sets, add all elements
   - Intersection: Iterate through smaller set, check membership in larger
   - Difference: Iterate through first set, exclude items in second
"""

def demonstrate_set_internals():
    """Demonstrate set internal behavior and operations"""
    
    print("\n=== SET INTERNALS EXAMPLES ===")
    
    # Set operations and their efficiency
    set1 = set(range(1000))
    set2 = set(range(500, 1500))
    
    import time
    
    # Union operation
    start = time.time()
    union_result = set1 | set2
    union_time = time.time() - start
    
    # Intersection operation
    start = time.time()
    intersection_result = set1 & set2
    intersection_time = time.time() - start
    
    print(f"Union time: {union_time:.6f}s, Result size: {len(union_result)}")
    print(f"Intersection time: {intersection_time:.6f}s, Result size: {len(intersection_result)}")
    
    # Membership testing efficiency
    large_list = list(range(10000))
    large_set = set(range(10000))
    
    # Test membership in list vs set
    start = time.time()
    result = 9999 in large_list
    list_search_time = time.time() - start
    
    start = time.time()
    result = 9999 in large_set
    set_search_time = time.time() - start
    
    print(f"\nSearch in list: {list_search_time:.8f}s")
    print(f"Search in set: {set_search_time:.8f}s")


# ============================================================================
# TUPLE - Immutable Sequence
# ============================================================================

"""
TUPLE INTERNALS:

1. IMMUTABLE ARRAY:
   - Fixed-size array of object pointers
   - Cannot be modified after creation
   - Memory layout similar to list but immutable

2. MEMORY EFFICIENCY:
   - More memory efficient than lists (no over-allocation)
   - Can be used as dictionary keys (if contains only hashable items)
   - Python caches small tuples for performance

3. OPERATIONS COMPLEXITY:
   - Access: O(1)
   - Search: O(n)
   - No modification operations (immutable)

4. OPTIMIZATIONS:
   - Small tuple caching (length 0-20)
   - Hashable if all elements are hashable
   - Used internally by Python for function arguments
"""

def demonstrate_tuple_internals():
    """Demonstrate tuple internal behavior"""
    
    print("\n=== TUPLE INTERNALS EXAMPLES ===")
    
    import sys
    
    # Memory comparison: tuple vs list
    tuple_obj = tuple(range(100))
    list_obj = list(range(100))
    
    print(f"Tuple memory: {sys.getsizeof(tuple_obj)} bytes")
    print(f"List memory: {sys.getsizeof(list_obj)} bytes")
    print(f"Memory difference: {sys.getsizeof(list_obj) - sys.getsizeof(tuple_obj)} bytes")
    
    # Tuple as dictionary key
    coord_dict = {(0, 0): "origin", (1, 1): "diagonal"}
    print(f"\nTuple as dict key: {coord_dict[(0, 0)]}")
    
    # Tuple caching demonstration
    t1 = (1, 2, 3)
    t2 = (1, 2, 3)
    print(f"Small tuple caching - same object: {t1 is t2}")


# ============================================================================
# SORTING ALGORITHMS - Timsort Implementation
# ============================================================================

"""
PYTHON SORTING (TIMSORT):

1. TIMSORT ALGORITHM:
   - Hybrid stable sorting algorithm
   - Combines merge sort and insertion sort
   - Designed by Tim Peters for Python
   - Optimized for real-world data patterns

2. KEY FEATURES:
   - Stable: Equal elements maintain relative order
   - Adaptive: Performs better on partially sorted data
   - Time Complexity: O(n log n) worst case, O(n) best case
   - Space Complexity: O(n)

3. ALGORITHM DETAILS:
   - Identifies "runs" (already sorted subsequences)
   - Uses insertion sort for small runs (< 64 elements)
   - Merges runs using optimized merge algorithm
   - Galloping mode for highly structured data

4. OPTIMIZATIONS:
   - Binary insertion sort for small arrays
   - Galloping mode when one run consistently wins
   - Minimum run length calculation
   - Optimized merging strategies
"""

def demonstrate_sorting_internals():
    """Demonstrate Python's sorting behavior and performance"""
    
    print("\n=== SORTING (TIMSORT) EXAMPLES ===")
    
    import random
    import time
    
    # Test on different data patterns
    sizes = [10000, 50000, 100000]
    
    for size in sizes:
        print(f"\n--- Testing with {size} elements ---")
        
        # Random data
        random_data = [random.randint(1, 1000) for _ in range(size)]
        start = time.time()
        sorted(random_data)
        random_time = time.time() - start
        
        # Already sorted data (best case for Timsort)
        sorted_data = list(range(size))
        start = time.time()
        sorted(sorted_data)
        sorted_time = time.time() - start
        
        # Reverse sorted data
        reverse_data = list(range(size, 0, -1))
        start = time.time()
        sorted(reverse_data)
        reverse_time = time.time() - start
        
        print(f"Random data: {random_time:.6f}s")
        print(f"Sorted data: {sorted_time:.6f}s")
        print(f"Reverse data: {reverse_time:.6f}s")
        if random_time > 0:
            print(f"Sorted/Random ratio: {sorted_time/random_time:.4f}")
        else:
            print("Times too small to measure accurately")


def timsort_concepts():
    """Explain Timsort concepts with examples"""
    
    print("\n=== TIMSORT CONCEPTS ===")
    
    # Run identification
    data = [1, 2, 3, 7, 6, 5, 4, 10, 11, 12]
    print(f"Data: {data}")
    print("Timsort would identify runs:")
    print("Run 1: [1, 2, 3] (ascending)")
    print("Run 2: [7, 6, 5, 4] (descending, will be reversed)")
    print("Run 3: [10, 11, 12] (ascending)")
    
    # Stable sorting demonstration
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person('{self.name}', {self.age})"
    
    people = [
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 25),
        Person("David", 30)
    ]
    
    # Sort by age - stable sort preserves relative order for equal ages
    sorted_people = sorted(people, key=lambda p: p.age)
    print(f"\nOriginal order: {people}")
    print(f"Sorted by age (stable): {sorted_people}")


# ============================================================================
# STRING INTERNALS
# ============================================================================

"""
STRING INTERNALS:

1. IMMUTABLE UNICODE OBJECTS:
   - Strings are immutable sequences of Unicode code points
   - Internal representation varies based on content (ASCII, Latin-1, UCS-2, UCS-4)
   - String interning for small strings and identifiers

2. MEMORY OPTIMIZATIONS:
   - Compact representation based on character range
   - ASCII strings use 1 byte per character
   - String interning saves memory for common strings

3. OPERATIONS:
   - Concatenation creates new objects
   - Slicing may share memory (copy-on-write in some cases)
   - String methods return new string objects
"""

def demonstrate_string_internals():
    """Demonstrate string internal behavior"""
    
    print("\n=== STRING INTERNALS EXAMPLES ===")
    
    import sys
    import time
    
    # String interning
    s1 = "hello"
    s2 = "hello"
    s3 = "".join(["h", "e", "l", "l", "o"])
    
    print(f"s1 is s2 (interned): {s1 is s2}")
    print(f"s1 is s3 (not interned): {s1 is s3}")
    
    # Memory usage for different string types
    ascii_str = "hello world"
    unicode_str = "hello 世界"
    
    print(f"\nASCII string memory: {sys.getsizeof(ascii_str)} bytes")
    print(f"Unicode string memory: {sys.getsizeof(unicode_str)} bytes")
    
    # String concatenation performance
    # Inefficient way
    start = time.time()
    result = ""
    for i in range(1000):
        result += str(i)
    inefficient_time = time.time() - start
    
    # Efficient way
    start = time.time()
    result = "".join(str(i) for i in range(1000))
    efficient_time = time.time() - start
    
    print(f"\nInefficient concatenation: {inefficient_time:.6f}s")
    print(f"Efficient join: {efficient_time:.6f}s")
    if efficient_time > 0:
        print(f"Speedup: {inefficient_time/efficient_time:.2f}x")
    else:
        print("Join operation is extremely efficient!")


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("PYTHON BUILT-IN DATA STRUCTURES: INTERNAL IMPLEMENTATION")
    print("=" * 60)
    
    demonstrate_dict_internals()
    demonstrate_list_internals()
    demonstrate_set_internals()
    demonstrate_tuple_internals()
    demonstrate_sorting_internals()
    timsort_concepts()
    demonstrate_string_internals()
    
    print("\n" + "=" * 60)
    print("SUMMARY OF TIME COMPLEXITIES:")
    print("=" * 60)
    
    complexity_summary = """
    DICTIONARY (Hash Table):
    - Access/Insert/Delete: O(1) average, O(n) worst case
    - Space: O(n)
    
    LIST (Dynamic Array):
    - Access by index: O(1)
    - Append: O(1) amortized
    - Insert/Delete: O(n)
    - Search: O(n)
    
    SET (Hash Table):
    - Add/Remove/Contains: O(1) average, O(n) worst case
    - Set operations: O(min(len(s1), len(s2)))
    
    TUPLE (Immutable Array):
    - Access: O(1)
    - Search: O(n)
    - Immutable - no modification operations
    
    SORTING (Timsort):
    - Best case: O(n) - already sorted
    - Average/Worst case: O(n log n)
    - Space: O(n)
    - Stable and adaptive
    
    STRING (Immutable Unicode):
    - Access: O(1)
    - Search: O(n)
    - Concatenation: O(n) - creates new object
    """
    
    print(complexity_summary)
