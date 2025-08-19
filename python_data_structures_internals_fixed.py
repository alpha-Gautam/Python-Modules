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
   - Since Python 3.7+, dictionaries maintain insertion order (ordered dict behavior)
   - Uses a compact representation to save memory

2. MEMORY LAYOUT (Python 3.6+):
   OLD WAY (before 3.6):
   [hash, key, value] [hash, key, value] [empty] [hash, key, value] [empty] [empty]
   
   NEW WAY (3.6+):
   INDEX TABLE: [1, -1, 0, -1, 2, -1]  # points to combined table
   COMBINED:    [(hash1, key1, val1), (hash2, key2, val2), (hash3, key3, val3)]
   
   BENEFITS:
   - 20-25% memory savings
   - Preserves insertion order as side effect
   - Better cache locality

3. COLLISION RESOLUTION:
   - Uses "open addressing" with pseudo-random probing
   - When slot is occupied, uses a deterministic sequence to find next slot
   - Probing sequence: i, i+1, i+4, i+9, i+16, ... (i + j^2)
   - Resizes when load factor reaches 2/3 to maintain performance

4. HASH FUNCTION:
   - Built-in hash() uses SipHash algorithm for strings (security)
   - Integers hash to themselves (with some modifications)
   - Custom objects can implement __hash__ and __eq__
"""

def demonstrate_dict_internals():
    print("=== DICTIONARY HASH EXAMPLES ===")
    
    # Show hash values for different types
    print(f"hash('hello'): {hash('hello')}")
    print(f"hash(42): {hash(42)}")
    print(f"hash((1, 2)): {hash((1, 2))}")
    
    # Show memory growth
    d = {}
    print(f"\nInitial dict size: {sys.getsizeof(d)} bytes")
    
    d['a'] = 1
    print(f"After 1 elements: {sys.getsizeof(d)} bytes")
    
    for i, char in enumerate('bcde'):
        d[char] = i + 2
    print(f"After 5 elements: {sys.getsizeof(d)} bytes")
    
    for i in range(6, 10):
        d[f'key{i}'] = i
    print(f"After 9 elements: {sys.getsizeof(d)} bytes")
    
    # Insertion order preservation (Python 3.7+)
    ordered_dict = {}
    for key in ['c', 'a', 'b']:
        ordered_dict[key] = key.upper()
    
    print(f"\nInsertion order preserved: {list(ordered_dict.keys())}")


# ============================================================================
# LIST - Dynamic Array Implementation
# ============================================================================

"""
LIST INTERNALS:

1. DYNAMIC ARRAY STRUCTURE:
   - Implemented as a dynamic array (like C++'s vector)
   - Stores pointers to Python objects, not objects themselves
   - Over-allocates memory to amortize the cost of growth

2. MEMORY LAYOUT:
   [ob_refcnt][ob_type][ob_size][ob_item][allocated][*ob_item]
   
   Where:
   - ob_size: current number of items
   - allocated: number of slots available
   - ob_item: array of pointers to Python objects

3. GROWTH STRATEGY:
   - When full, allocates new_size = (old_size >> 1) + old_size + 3
   - For small lists: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88...
   - For large lists: approximately 1.125x growth factor
   - This makes append() amortized O(1)

4. OPERATIONS COMPLEXITY:
   - Access by index: O(1)
   - Append: Amortized O(1), worst case O(n) when resizing
   - Insert at beginning: O(n) - must shift all elements
   - Delete by index: O(n) - must shift elements after deletion
   - Search: O(n) - linear scan required
"""

def demonstrate_list_internals():
    print("\n=== LIST INTERNALS EXAMPLES ===")
    
    # Show memory allocation pattern
    print("List growth pattern:")
    lst = []
    prev_size = 0
    
    for i in range(1, 10):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != prev_size:
            print(f"Length {i}: {current_size} bytes (capacity increased)")
            prev_size = current_size
    
    # Performance comparison
    large_list = list(range(100000))
    
    # Append (fast)
    start = time.time()
    test_list = []
    for i in range(1000):
        test_list.append(i)
    append_time = time.time() - start
    
    # Insert at beginning (slow)
    start = time.time()
    test_list = []
    for i in range(1000):
        test_list.insert(0, i)
    insert_time = time.time() - start
    
    print(f"\nAppend time: {append_time:.8f}s")
    print(f"Insert at beginning time: {insert_time:.8f}s")


# ============================================================================
# SET - Hash Table for Uniqueness
# ============================================================================

"""
SET INTERNALS:

1. HASH TABLE STRUCTURE:
   - Similar to dict but stores only keys, no values
   - Uses same collision resolution as dictionaries
   - Automatically prevents duplicates through hash uniqueness

2. SET OPERATIONS OPTIMIZATION:
   - Union (A | B): Iterate through smaller set, add to larger
   - Intersection (A & B): Iterate through smaller set, check membership in larger
   - Difference (A - B): Iterate through A, exclude items in B
   - Always chooses the most efficient algorithm based on set sizes

3. HASH REQUIREMENTS:
   - Items must be hashable (implement __hash__ and __eq__)
   - Immutable types: int, str, tuple (with hashable contents)
   - Mutable types: list, dict, set are NOT hashable
"""

def demonstrate_set_internals():
    print("\n=== SET INTERNALS EXAMPLES ===")
    
    # Set operations performance
    set1 = set(range(1000))
    set2 = set(range(500, 1500))
    
    start = time.time()
    union_result = set1 | set2
    union_time = time.time() - start
    
    start = time.time()
    intersection_result = set1 & set2
    intersection_time = time.time() - start
    
    print(f"Union time: {union_time:.6f}s, Result size: {len(union_result)}")
    print(f"Intersection time: {intersection_time:.6f}s, Result size: {len(intersection_result)}")
    
    # Membership testing comparison
    large_list = list(range(100000))
    large_set = set(large_list)
    search_item = 99999
    
    start = time.time()
    result1 = search_item in large_list
    list_time = time.time() - start
    
    start = time.time()
    result2 = search_item in large_set
    set_time = time.time() - start
    
    print(f"\nSearch in list: {list_time:.8f}s")
    print(f"Search in set: {set_time:.8f}s")


# ============================================================================
# TUPLE - Immutable Sequence
# ============================================================================

"""
TUPLE INTERNALS:

1. IMMUTABLE ARRAY:
   - Fixed-size array of object pointers
   - Cannot change size or contents after creation
   - More memory efficient than lists (no over-allocation needed)

2. MEMORY OPTIMIZATION:
   - Small tuples (size 0-20) are cached and reused
   - Empty tuple is a singleton object
   - Immutability enables aggressive optimizations

3. HASHABILITY:
   - Tuples are hashable if all their elements are hashable
   - Can be used as dictionary keys and set elements
   - Hash is computed from all elements
"""

def demonstrate_tuple_internals():
    print("\n=== TUPLE INTERNALS EXAMPLES ===")
    
    # Memory comparison
    tuple_data = tuple(range(100))
    list_data = list(range(100))
    
    tuple_size = sys.getsizeof(tuple_data)
    list_size = sys.getsizeof(list_data)
    
    print(f"Tuple memory: {tuple_size} bytes")
    print(f"List memory: {list_size} bytes")
    print(f"Memory difference: {list_size - tuple_size} bytes")
    
    # Tuple as dictionary key
    Point = namedtuple('Point', ['x', 'y'])
    distances = {(0, 0): "origin", (1, 1): "diagonal"}
    print(f"\nTuple as dict key: {distances[(0, 0)]}")
    
    # Small tuple caching
    t1 = (1, 2)
    t2 = (1, 2)
    print(f"Small tuple caching - same object: {t1 is t2}")


# ============================================================================
# SORTING (Timsort Algorithm)
# ============================================================================

"""
TIMSORT INTERNALS:

1. HYBRID ALGORITHM:
   - Combines merge sort and insertion sort
   - Uses insertion sort for small runs (< 64 elements)
   - Uses merge sort for larger sequences
   - Adaptive: takes advantage of existing order

2. RUN DETECTION:
   - Finds existing sorted subsequences ("runs")
   - Extends short runs using insertion sort
   - Reverses strictly descending runs
   - Maintains stack of pending runs for merging

3. GALLOPING MODE:
   - When one run consistently "wins" during merge
   - Switches to exponential search instead of linear
   - Dramatically speeds up merging of mostly-sorted data

4. STABILITY:
   - Equal elements maintain their relative order
   - Important for complex sorting scenarios
   - Achieved through careful merge implementation
"""

Person = namedtuple('Person', ['name', 'age'])

def demonstrate_sorting_internals():
    print("\n=== SORTING (TIMSORT) EXAMPLES ===")
    
    # Test different data patterns
    sizes = [10000, 50000, 100000]
    
    for size in sizes:
        print(f"\n--- Testing with {size} elements ---")
        
        # Random data
        random_data = [random.randint(1, 1000) for _ in range(size)]
        start = time.time()
        sorted(random_data)
        random_time = time.time() - start
        
        # Already sorted data
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
    
    # Demonstrate run identification concept
    print(f"\n=== TIMSORT CONCEPTS ===")
    data = [1, 2, 3, 7, 6, 5, 4, 10, 11, 12]
    print(f"Data: {data}")
    print("Timsort would identify runs:")
    print("Run 1: [1, 2, 3] (ascending)")
    print("Run 2: [7, 6, 5, 4] (descending, will be reversed)")
    print("Run 3: [10, 11, 12] (ascending)")
    
    # Stability demonstration
    people = [Person('Alice', 25), Person('Bob', 30), Person('Charlie', 25), Person('David', 30)]
    print(f"\nOriginal order: {people}")
    sorted_people = sorted(people, key=lambda p: p.age)
    print(f"Sorted by age (stable): {sorted_people}")


# ============================================================================
# STRING - Immutable Unicode Sequence
# ============================================================================

"""
STRING INTERNALS:

1. UNICODE IMPLEMENTATION:
   - Variable-width encoding based on content
   - ASCII: 1 byte per character (for ASCII-only strings)
   - Latin-1: 1 byte per character (for chars 0-255)
   - UCS-2: 2 bytes per character (for BMP characters)
   - UCS-4: 4 bytes per character (for all Unicode)

2. STRING INTERNING:
   - Common strings are cached in a global dictionary
   - Literals, identifiers, and some runtime strings are interned
   - sys.intern() can manually intern strings
   - Saves memory for frequently used strings

3. IMMUTABILITY IMPLICATIONS:
   - Every string operation creates a new string object
   - String concatenation with + is inefficient for many operations
   - str.join() is optimized for building strings from sequences
   - String formatting (f-strings, format()) is optimized
"""

def demonstrate_string_internals():
    print("\n=== STRING INTERNALS EXAMPLES ===")
    
    # String interning
    s1 = "hello"
    s2 = "hello"
    s3 = "".join(['h', 'e', 'l', 'l', 'o'])
    
    print(f"s1 is s2 (interned): {s1 is s2}")
    print(f"s1 is s3 (not interned): {s1 is s3}")
    
    # Memory usage of different encodings
    ascii_string = "hello world"
    unicode_string = "hello 🌍"
    
    print(f"\nASCII string memory: {sys.getsizeof(ascii_string)} bytes")
    print(f"Unicode string memory: {sys.getsizeof(unicode_string)} bytes")
    
    # Concatenation performance
    start = time.time()
    result = ""
    for i in range(1000):
        result += str(i)
    inefficient_time = time.time() - start
    
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
    demonstrate_string_internals()
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE SUMMARY:")
    print("=" * 60)
    print("""
🔹 DICTIONARIES: Highly optimized hash tables with order preservation,
   compact memory layout, and sophisticated collision handling.

🔹 LISTS: Dynamic arrays with intelligent over-allocation strategies
   for amortized O(1) append operations and efficient random access.

🔹 SETS: Hash tables optimized for membership testing and set operations,
   with algorithms that adapt based on relative set sizes.

🔹 TUPLES: Memory-efficient immutable sequences with caching optimizations
   for small tuples and the ability to serve as dictionary keys.

🔹 SORTING: Timsort algorithm that adapts to data patterns, maintains
   stability, and achieves near-optimal performance on real-world data.

🔹 STRINGS: Immutable Unicode sequences with variable-width encoding,
   interning for common strings, and optimized operations for building.

💡 GENERAL PRINCIPLES:
   • Python prioritizes developer productivity while maintaining performance
   • Data structures are heavily optimized for common use patterns
   • Memory layout and algorithmic choices reflect real-world usage
   • The standard library provides tools optimized for their specific purposes
""")
