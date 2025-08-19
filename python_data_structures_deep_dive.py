"""
DEEP DIVE: Python Data Structures Implementation Details

This file provides in-depth explanations of how Python implements its core data structures
at the C level and the algorithms they use behind the scenes.
"""

# ============================================================================
# DICTIONARY IMPLEMENTATION DETAILS
# ============================================================================

"""
DICTIONARY HASH TABLE IMPLEMENTATION:

1. PRE-PYTHON 3.6 (Classical Hash Table):
   - Open addressing with pseudo-random probing
   - Each slot contained: [hash, key, value] or empty
   - Memory layout: [slot1][slot2][slot3]...[slotN]
   - No order preservation

2. PYTHON 3.6+ (Compact Dict):
   Combined Table: Stores [hash, key, value] sequentially
   Sparse Index: Array of indices pointing to combined table entries
   
   Example:
   d = {'a': 1, 'b': 2}
   
   Sparse Index: [empty, 0, empty, 1, empty, ...]
   Combined Table: [(hash('a'), 'a', 1), (hash('b'), 'b', 2)]

3. COLLISION RESOLUTION:
   Uses random probing with the formula:
   j = (5*j + 1 + perturb) & mask
   where perturb >>= 5 each iteration

4. RESIZING STRATEGY:
   - Starts with size 8
   - Resizes when 2/3 full (load factor 0.67)
   - New size = 4 * used_slots (if used > 50k, else 2 * used_slots)

5. HASH FUNCTION:
   - Uses SipHash for strings (security against hash DoS)
   - For integers: hash(x) = x (if x fits in a machine word)
   - For tuples: combines hashes of elements with XOR and rotation
"""

def explain_dict_collision_handling():
    """Demonstrate how dictionary handles hash collisions"""
    
    print("=== DICTIONARY COLLISION HANDLING ===")
    
    # Create strings that might collide (simplified example)
    class BadHash:
        def __init__(self, value):
            self.value = value
        
        def __hash__(self):
            # Intentionally bad hash function to force collisions
            return len(str(self.value))
        
        def __eq__(self, other):
            return self.value == other.value
        
        def __repr__(self):
            return f"BadHash({self.value})"
    
    # These will all have the same hash (length 1)
    collision_dict = {}
    items = [BadHash(1), BadHash(2), BadHash(3), BadHash(4)]
    
    for i, item in enumerate(items):
        collision_dict[item] = i
        print(f"Added {item} with hash {hash(item)}")
    
    print(f"Final dict: {collision_dict}")
    print("All items stored despite hash collisions due to open addressing")


# ============================================================================
# LIST IMPLEMENTATION DETAILS
# ============================================================================

"""
LIST DYNAMIC ARRAY IMPLEMENTATION:

1. C STRUCTURE (PyListObject):
   typedef struct {
       PyObject_VAR_HEAD
       PyObject **ob_item;     // Pointer to array of PyObject pointers
       Py_ssize_t allocated;   // Number of allocated slots
   } PyListObject;

2. GROWTH ALGORITHM:
   new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6);
   new_allocated += newsize;
   
   Simplified: ~1.125x growth factor with some adjustments

3. MEMORY LAYOUT:
   [PyListObject][pointer1][pointer2]...[pointerN][unused_slots]
   
   Each pointer points to the actual Python object elsewhere in memory

4. OPERATIONS IMPLEMENTATION:

   APPEND (list_append):
   - Check if resize needed
   - If needed, reallocate with growth factor
   - Set new item at end
   - Increment size

   INSERT (list_insert):
   - Shift all elements after insertion point
   - Requires moving O(n) pointers
   - May trigger reallocation

   DELETE (list_remove):
   - Find item (O(n) search)
   - Shift all elements after deletion point
   - Decrement size

5. SLICING OPTIMIZATION:
   - Creates new list object
   - Copies only the pointer references (shallow copy)
   - Objects themselves are not duplicated
"""

def demonstrate_list_memory_behavior():
    """Show how list memory allocation works"""
    
    print("\n=== LIST MEMORY ALLOCATION ===")
    
    import sys
    
    # Demonstrate over-allocation
    lst = []
    print("List growth and over-allocation:")
    print("Length | Memory | Estimated Capacity")
    print("-" * 35)
    
    for i in range(20):
        lst.append(i)
        memory = sys.getsizeof(lst)
        # Rough estimation of capacity based on memory
        # 64 bytes overhead + 8 bytes per pointer (64-bit system)
        estimated_capacity = (memory - 64) // 8
        print(f"{len(lst):6} | {memory:6} | {estimated_capacity:10}")


# ============================================================================
# SET IMPLEMENTATION DETAILS
# ============================================================================

"""
SET HASH TABLE IMPLEMENTATION:

1. SIMILAR TO DICT BUT SIMPLER:
   - Stores only keys, no values
   - Uses same collision resolution as dict
   - Maintains uniqueness through hash lookups

2. SET OPERATIONS ALGORITHMS:

   UNION (set_union):
   for item in other:
       result.add(item)
   
   INTERSECTION (set_intersection):
   for item in smaller_set:
       if item in larger_set:
           result.add(item)
   
   DIFFERENCE (set_difference):
   for item in self:
       if item not in other:
           result.add(item)

3. OPTIMIZATION:
   - For very small sets (< 5 elements), linear search might be faster
   - Set operations create new set objects
   - In-place operations (|=, &=, -=) modify existing set
"""

def demonstrate_set_operations_performance():
    """Compare different set operation implementations"""
    
    print("\n=== SET OPERATIONS PERFORMANCE ===")
    
    import time
    
    # Create test sets
    set1 = set(range(0, 10000, 2))      # Even numbers
    set2 = set(range(0, 10000, 3))      # Multiples of 3
    
    # Union operation
    start = time.time()
    union_builtin = set1 | set2
    builtin_time = time.time() - start
    
    # Manual union (less efficient)
    start = time.time()
    union_manual = set1.copy()
    for item in set2:
        union_manual.add(item)
    manual_time = time.time() - start
    
    print(f"Built-in union: {builtin_time:.6f}s")
    print(f"Manual union: {manual_time:.6f}s")
    if builtin_time > 0:
        print(f"Speedup: {manual_time/builtin_time:.2f}x")
    else:
        print("Built-in operations are extremely optimized!")
    print(f"Results equal: {union_builtin == union_manual}")


# ============================================================================
# TIMSORT ALGORITHM DETAILS
# ============================================================================

"""
TIMSORT IMPLEMENTATION:

1. HYBRID ALGORITHM:
   - Merge sort for general case
   - Insertion sort for small runs (< 64 elements)
   - Galloping mode for structured data

2. RUN DETECTION:
   - Scans for already-sorted subsequences
   - Reverses decreasing runs to make them increasing
   - Minimum run length calculated as: minrun = n//64 + (1 if n%64 else 0)

3. MERGING STRATEGY:
   - Maintains stack of pending runs
   - Merges when stack invariants violated:
     * runlen[i-3] > runlen[i-2] + runlen[i-1]
     * runlen[i-2] > runlen[i-1]

4. GALLOPING MODE:
   - When one run consistently "wins" during merge
   - Uses binary search to find merge points
   - Exits galloping if runs become more balanced

5. OPTIMIZATIONS:
   - Binary insertion sort for small runs
   - Merge optimization with temporary space
   - Special handling for equal elements

EXAMPLE TIMSORT STEPS:
Input: [5,2,4,6,1,3,8,7,9]

Step 1: Find runs
- [5] (length 1, too short)
- [2,4,6] (increasing run)
- [1] (length 1, too short) 
- [3] (length 1, too short)
- [8] (length 1, too short)
- [7,9] (increasing run)

Step 2: Extend short runs with insertion sort
- [2,4,5,6] (extended first run)
- [1,3,8] (merged and sorted short runs)
- [7,9] (already good)

Step 3: Merge runs
- Merge [2,4,5,6] and [1,3,8] → [1,2,3,4,5,6,8]
- Merge with [7,9] → [1,2,3,4,5,6,7,8,9]
"""

def demonstrate_timsort_behavior():
    """Show Timsort's adaptive behavior"""
    
    print("\n=== TIMSORT ADAPTIVE BEHAVIOR ===")
    
    import time
    import random
    
    size = 50000
    
    # Test different data patterns
    test_cases = [
        ("Random", [random.randint(1, 1000) for _ in range(size)]),
        ("Sorted", list(range(size))),
        ("Reverse", list(range(size, 0, -1))),
        ("Nearly sorted", list(range(size))),
        ("Few unique", [random.randint(1, 10) for _ in range(size)]),
    ]
    
    # Make "nearly sorted" actually nearly sorted
    nearly_sorted = test_cases[3][1]
    for _ in range(size // 100):  # Shuffle 1% of elements
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
    
    print("Data Pattern     | Time (ms) | Relative Performance")
    print("-" * 50)
    
    random_time = None
    for name, data in test_cases:
        start = time.time()
        sorted(data)
        elapsed = (time.time() - start) * 1000  # Convert to milliseconds
        
        if name == "Random":
            random_time = elapsed
            relative = 1.0
        else:
            relative = elapsed / random_time if random_time else 1.0
        
        print(f"{name:15} | {elapsed:7.2f}   | {relative:6.2f}x")


# ============================================================================
# STRING IMPLEMENTATION DETAILS
# ============================================================================

"""
STRING IMPLEMENTATION:

1. UNICODE OBJECTS (Python 3):
   - All strings are Unicode
   - Variable-width internal representation
   - ASCII: 1 byte per character
   - Latin-1: 1 byte per character  
   - UCS-2: 2 bytes per character
   - UCS-4: 4 bytes per character

2. STRING INTERNING:
   - Small strings and identifiers are interned
   - Saves memory for common strings
   - Only strings that look like identifiers are automatically interned

3. COMPACT REPRESENTATION:
   typedef struct {
       PyObject_HEAD
       Py_ssize_t length;
       Py_hash_t hash;
       struct {
           unsigned int interned:2;
           unsigned int kind:3;      // ASCII, Latin-1, UCS-2, UCS-4
           unsigned int compact:1;
           unsigned int ascii:1;
           unsigned int ready:1;
       } state;
       wchar_t *wstr;
   } PyUnicodeObject;

4. STRING OPERATIONS:
   - All operations create new string objects (immutable)
   - Concatenation with + creates temporary objects
   - str.join() is more efficient for multiple concatenations
   - Slicing may share memory in some implementations
"""

def demonstrate_string_optimization():
    """Show string optimization techniques"""
    
    print("\n=== STRING OPTIMIZATION TECHNIQUES ===")
    
    import time
    import sys
    
    # String interning examples
    print("String Interning:")
    s1 = "hello_world"
    s2 = "hello_world"
    s3 = "hello" + "_" + "world"
    s4 = "hello world"  # Space prevents automatic interning
    s5 = "hello world"
    
    print(f"s1 is s2 (same literal): {s1 is s2}")
    print(f"s1 is s3 (computed): {s1 is s3}")
    print(f"s4 is s5 (with space): {s4 is s5}")
    
    # Manual interning
    import sys
    s6 = sys.intern("hello world")
    s7 = sys.intern("hello world")
    print(f"Manually interned: {s6 is s7}")
    
    # Concatenation performance
    print("\nConcatenation Performance (10000 operations):")
    
    # Inefficient: repeated concatenation
    start = time.time()
    result = ""
    for i in range(10000):
        result += str(i) + ","
    concat_time = time.time() - start
    
    # Efficient: join method
    start = time.time()
    parts = []
    for i in range(10000):
        parts.append(str(i))
    result = ",".join(parts)
    join_time = time.time() - start
    
    # Most efficient: generator with join
    start = time.time()
    result = ",".join(str(i) for i in range(10000))
    generator_time = time.time() - start
    
    print(f"Concatenation: {concat_time:.4f}s")
    print(f"List + join:   {join_time:.4f}s")
    print(f"Generator:     {generator_time:.4f}s")
    print(f"Join speedup:  {concat_time/join_time:.1f}x")
    

# ============================================================================
# MEMORY MANAGEMENT INSIGHTS
# ============================================================================

def analyze_memory_usage():
    """Analyze memory usage patterns of different data structures"""
    
    print("\n=== MEMORY USAGE ANALYSIS ===")
    
    import sys
    
    # Compare memory usage
    n = 1000
    
    # Different ways to store the same data
    data_structures = [
        ("List of integers", list(range(n))),
        ("Tuple of integers", tuple(range(n))),
        ("Set of integers", set(range(n))),
        ("Dict {i: i}", {i: i for i in range(n)}),
        ("Dict {i: None}", {i: None for i in range(n)}),
        ("String of digits", "".join(str(i%10) for i in range(n))),
    ]
    
    print(f"Memory usage for {n} integers:")
    print("Data Structure        | Memory (bytes) | Bytes per item")
    print("-" * 55)
    
    for name, ds in data_structures:
        memory = sys.getsizeof(ds)
        per_item = memory / n
        print(f"{name:20} | {memory:10} | {per_item:10.1f}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("PYTHON DATA STRUCTURES: DEEP IMPLEMENTATION DIVE")
    print("=" * 60)
    
    explain_dict_collision_handling()
    demonstrate_list_memory_behavior()
    demonstrate_set_operations_performance()
    demonstrate_timsort_behavior()
    demonstrate_string_optimization()
    analyze_memory_usage()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
    1. DICTIONARIES: Use sophisticated hash tables with collision resolution
       and memory optimization. Order preservation since Python 3.7.
    
    2. LISTS: Dynamic arrays with over-allocation for amortized O(1) append.
       Insertion/deletion in middle is expensive due to element shifting.
    
    3. SETS: Hash tables optimized for membership testing and set operations.
       Very efficient for uniqueness checking and mathematical set operations.
    
    4. TUPLES: Immutable, memory-efficient sequences. Can be dictionary keys
       and benefit from caching for small tuples.
    
    5. SORTING: Timsort is adaptive and stable, performing exceptionally well
       on partially sorted data while maintaining O(n log n) worst-case.
    
    6. STRINGS: Immutable Unicode objects with variable-width encoding and
       interning for common strings. Concatenation creates new objects.
    
    7. MEMORY: Choose data structures based on use case - lists for ordered
       data with modifications, tuples for immutable sequences, sets for
       uniqueness, and dicts for key-value mappings.
    """)
