"""
PYTHON BUILT-IN DATA STRUCTURES: WHAT HAPPENS BEHIND THE SCENES

A comprehensive guide to understanding how Python's core data structures work internally.
This explains the algorithms, memory management, and performance characteristics.
"""

# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================

"""
QUICK OVERVIEW:

📊 DICTIONARY: Hash table with order preservation (Python 3.7+)
   - O(1) average access time
   - Uses sophisticated collision resolution
   - 20-25% memory savings with compact representation

📋 LIST: Dynamic array with smart memory allocation
   - O(1) append, O(n) insert/delete in middle
   - Over-allocates memory for performance
   - Great for ordered data that changes

🔗 SET: Hash table optimized for uniqueness
   - O(1) membership testing
   - Efficient set operations (union, intersection)
   - Perfect for removing duplicates

📦 TUPLE: Immutable, memory-efficient sequence
   - Cannot be changed after creation
   - More memory efficient than lists
   - Can be used as dictionary keys

🔄 SORTING: Timsort algorithm (hybrid merge/insertion sort)
   - Adaptive: faster on partially sorted data
   - Stable: preserves order of equal elements
   - O(n) best case, O(n log n) worst case

📝 STRING: Immutable Unicode sequences
   - Variable-width encoding (1-4 bytes per character)
   - String interning for memory efficiency
   - Concatenation creates new objects
"""

# ============================================================================
# 1. DICTIONARY - THE SMART HASH TABLE
# ============================================================================

def explain_dictionary_internals():
    """
    DICTIONARY BEHIND THE SCENES:
    
    Think of a dictionary like a smart filing cabinet:
    - Uses a hash function to quickly find the right "drawer" 
    - Handles conflicts when multiple items want the same drawer
    - Since Python 3.7, remembers the order you put things in
    """
    
    print("=== HOW DICTIONARIES WORK ===")
    
    # 1. Hash Function Magic
    print("1. Hash Function converts keys to numbers:")
    examples = ['apple', 'banana', 'cherry']
    for key in examples:
        print(f"   '{key}' → hash: {hash(key)}")
    
    # 2. Memory Layout Evolution
    print("\n2. Memory Layout (Python 3.6+ optimization):")
    print("   OLD WAY: [hash|key|value] [hash|key|value] [empty] [hash|key|value]")
    print("   NEW WAY: Separate index + packed data")
    print("   INDEX:  [1, empty, 0, empty, 2, ...]")
    print("   DATA:   [(hash1,key1,val1), (hash2,key2,val2), (hash3,key3,val3)]")
    print("   BENEFIT: 20-25% memory savings + maintains insertion order")
    
    # 3. Collision Handling
    print("\n3. Collision Handling:")
    print("   When two keys hash to same location:")
    print("   - Uses 'open addressing' - finds next available spot")
    print("   - Uses random probing pattern to avoid clustering")
    print("   - Resizes table when 2/3 full to maintain performance")


def demonstrate_dict_performance():
    """Show why dictionaries are so fast"""
    
    import time
    
    # Create test data
    data = {f"key_{i}": i for i in range(100000)}
    keys_to_find = [f"key_{i}" for i in range(0, 100000, 1000)]
    
    # Dictionary lookup (O(1))
    start = time.time()
    for key in keys_to_find:
        value = data[key]
    dict_time = time.time() - start
    
    # List search equivalent (O(n))
    data_list = [(f"key_{i}", i) for i in range(100000)]
    start = time.time()
    for key in keys_to_find:
        for k, v in data_list:
            if k == key:
                value = v
                break
    list_time = time.time() - start
    
    print(f"\n=== DICTIONARY PERFORMANCE ===")
    print(f"Dictionary lookup: {dict_time:.6f}s")
    print(f"List search:       {list_time:.6f}s")
    if dict_time > 0:
        print(f"Dictionary is {list_time/dict_time:.0f}x faster!")
    else:
        print("Dictionary lookup is practically instantaneous!")


# ============================================================================
# 2. LIST - THE SMART EXPANDING ARRAY
# ============================================================================

def explain_list_internals():
    """
    LIST BEHIND THE SCENES:
    
    Think of a list like a smart parking garage:
    - Has numbered parking spots (indices) for quick access
    - When full, builds additional floors (over-allocation)
    - Moving cars in the middle requires shifting all cars behind them
    """
    
    print("\n=== HOW LISTS WORK ===")
    
    print("1. Memory Layout:")
    print("   [Header][ptr1][ptr2][ptr3]...[ptrN][unused][unused]...")
    print("   Each pointer points to the actual Python object")
    print("   Over-allocates space to avoid frequent resizing")
    
    print("\n2. Growth Strategy:")
    print("   When full, allocates ~12.5% more space")
    print("   Example: 8 → 9 → 13 → 19 → 26 → 35 → 46...")
    print("   This makes append() very fast on average")
    
    print("\n3. Operations Cost:")
    print("   ✅ FAST:   Access by index, append to end")
    print("   ❌ SLOW:   Insert/delete in middle (must shift elements)")
    print("   ⚠️  MEDIUM: Search for value (must check each element)")


def demonstrate_list_performance():
    """Show list operation performance differences"""
    
    import time
    
    # Test different operations
    test_list = list(range(50000))
    
    # Fast: append
    start = time.time()
    for i in range(1000):
        test_list.append(i)
    append_time = time.time() - start
    
    # Slow: insert at beginning
    start = time.time()
    for i in range(1000):
        test_list.insert(0, i)
    insert_time = time.time() - start
    
    # Medium: search
    start = time.time()
    for i in range(1000):
        result = 25000 in test_list
    search_time = time.time() - start
    
    print(f"\n=== LIST OPERATION PERFORMANCE ===")
    print(f"Append 1000 items:       {append_time:.6f}s")
    print(f"Insert 1000 at start:    {insert_time:.6f}s")
    print(f"Search 1000 times:       {search_time:.6f}s")
    if append_time > 0:
        print(f"Insert is {insert_time/append_time:.0f}x slower than append")
        print(f"Search is {search_time/append_time:.0f}x slower than append")
    else:
        print("Append operation is practically instantaneous!")
        print("Insert is significantly slower than append")
        print("Search is significantly slower than append")


# ============================================================================
# 3. SET - THE UNIQUENESS ENFORCER
# ============================================================================

def explain_set_internals():
    """
    SET BEHIND THE SCENES:
    
    Think of a set like a smart bouncer at a club:
    - Keeps a list of everyone who's already inside (hash table)
    - Instantly recognizes if someone is trying to enter twice
    - Can quickly compare guest lists with other clubs
    """
    
    print("\n=== HOW SETS WORK ===")
    
    print("1. Hash Table (like dict but simpler):")
    print("   Stores only keys, no values")
    print("   Uses same collision resolution as dictionaries")
    print("   Automatically prevents duplicates")
    
    print("\n2. Set Operations are optimized:")
    print("   UNION (A | B):        Add all items from both sets")
    print("   INTERSECTION (A & B): Keep only items in both sets")
    print("   DIFFERENCE (A - B):   Keep items in A but not in B")
    print("   Algorithm: Always iterate through smaller set when possible")


def demonstrate_set_power():
    """Show set's unique capabilities"""
    
    print("\n=== SET POWER DEMONSTRATION ===")
    
    # Duplicate removal
    messy_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    clean_data = list(set(messy_data))
    print(f"Remove duplicates: {messy_data} → {clean_data}")
    
    # Fast membership testing
    large_list = list(range(100000))
    large_set = set(range(100000))
    
    import time
    
    # Test if item exists
    start = time.time()
    result = 99999 in large_list  # O(n) - slow
    list_time = time.time() - start
    
    start = time.time()
    result = 99999 in large_set   # O(1) - fast
    set_time = time.time() - start
    
    print(f"Find item in 100k elements:")
    print(f"  List: {list_time:.8f}s")
    print(f"  Set:  {set_time:.8f}s")
    if set_time > 0:
        print(f"  Set is {list_time/set_time:.0f}x faster!")
    else:
        print("  Set lookup is practically instantaneous!")
    
    # Set operations
    friends_alice = {'Bob', 'Charlie', 'David'}
    friends_bob = {'Alice', 'Charlie', 'Eve'}
    
    print(f"\nSet Operations:")
    print(f"Alice's friends: {friends_alice}")
    print(f"Bob's friends:   {friends_bob}")
    print(f"Mutual friends:  {friends_alice & friends_bob}")
    print(f"All friends:     {friends_alice | friends_bob}")


# ============================================================================
# 4. TUPLE - THE UNCHANGEABLE CONTAINER
# ============================================================================

def explain_tuple_internals():
    """
    TUPLE BEHIND THE SCENES:
    
    Think of a tuple like a sealed shipping container:
    - Once packed, contents cannot be changed
    - More compact than regular containers (lists)
    - Can be used as a unique identifier (hashable)
    """
    
    print("\n=== HOW TUPLES WORK ===")
    
    print("1. Immutable Array:")
    print("   Fixed size - no over-allocation needed")
    print("   Cannot add, remove, or change elements")
    print("   More memory efficient than lists")
    
    print("2. Hashable (if contents are hashable):")
    print("   Can be used as dictionary keys")
    print("   Can be stored in sets")
    print("   Enables powerful data structures")
    
    print("3. Optimizations:")
    print("   Small tuples are cached by Python")
    print("   Empty tuple is a singleton")
    print("   Used internally for function arguments")


def demonstrate_tuple_benefits():
    """Show tuple advantages"""
    
    import sys
    
    print("\n=== TUPLE BENEFITS ===")
    
    # Memory efficiency
    data = list(range(1000))
    tuple_version = tuple(data)
    list_version = list(data)
    
    print(f"Memory comparison (1000 items):")
    print(f"  Tuple: {sys.getsizeof(tuple_version)} bytes")
    print(f"  List:  {sys.getsizeof(list_version)} bytes")
    print(f"  Savings: {sys.getsizeof(list_version) - sys.getsizeof(tuple_version)} bytes")
    
    # Dictionary keys
    coordinates = {
        (0, 0): "origin",
        (1, 0): "right",
        (0, 1): "up",
        (1, 1): "diagonal"
    }
    print(f"\nTuples as dict keys: {coordinates[(1, 1)]}")
    
    # Tuple unpacking
    point = (3, 4)
    x, y = point
    print(f"Tuple unpacking: point {point} → x={x}, y={y}")


# ============================================================================
# 5. SORTING - THE INTELLIGENT ORGANIZER
# ============================================================================

def explain_sorting_internals():
    """
    TIMSORT BEHIND THE SCENES:
    
    Think of Timsort like a smart librarian:
    - Looks for books that are already in order (runs)
    - Uses different strategies for different situations
    - Remembers what worked well and adapts
    """
    
    print("\n=== HOW PYTHON SORTING (TIMSORT) WORKS ===")
    
    print("1. Hybrid Algorithm:")
    print("   Insertion sort: For small groups (< 64 items)")
    print("   Merge sort: For larger groups")
    print("   Galloping mode: When data has patterns")
    
    print("2. Adaptive Behavior:")
    print("   Finds already-sorted subsequences ('runs')")
    print("   Reverses decreasing runs to make them increasing")
    print("   Merges runs efficiently")
    
    print("3. Why it's special:")
    print("   ✅ STABLE: Equal items keep their relative order")
    print("   ✅ ADAPTIVE: Faster on partially sorted data")
    print("   ✅ OPTIMAL: O(n) best case, O(n log n) worst case")


def demonstrate_sorting_adaptiveness():
    """Show how Timsort adapts to different data patterns"""
    
    import time
    import random
    
    print("\n=== TIMSORT ADAPTIVENESS ===")
    
    size = 20000
    
    test_cases = [
        ("Random data", [random.randint(1, 1000) for _ in range(size)]),
        ("Already sorted", list(range(size))),
        ("Reverse sorted", list(range(size, 0, -1))),
        ("Mostly sorted", list(range(size))),
    ]
    
    # Mess up the "mostly sorted" data a bit
    mostly_sorted = test_cases[3][1]
    for _ in range(size // 50):  # Shuffle 2% of elements
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        mostly_sorted[i], mostly_sorted[j] = mostly_sorted[j], mostly_sorted[i]
    
    print("Data Pattern      | Time (ms) | Performance")
    print("-" * 45)
    
    for name, data in test_cases:
        start = time.time()
        sorted(data)
        elapsed = (time.time() - start) * 1000
        
        if name == "Random data":
            baseline = elapsed
            performance = "Baseline"
        else:
            if elapsed > 0:
                performance = f"{baseline/elapsed:.1f}x faster"
            else:
                performance = "Extremely fast"
        
        print(f"{name:15} | {elapsed:7.2f}   | {performance}")


# ============================================================================
# 6. STRING - THE IMMUTABLE TEXT HANDLER
# ============================================================================

def explain_string_internals():
    """
    STRING BEHIND THE SCENES:
    
    Think of strings like printed pages:
    - Once printed, cannot be changed (immutable)
    - Different ink types for different characters (encoding)
    - Common phrases are kept in a shared library (interning)
    """
    
    print("\n=== HOW STRINGS WORK ===")
    
    print("1. Unicode with Smart Encoding:")
    print("   ASCII characters: 1 byte each (a, b, c)")
    print("   Latin-1: 1 byte each (café)")
    print("   Unicode: 2-4 bytes each (🌟, 中文)")
    print("   Chooses most efficient encoding automatically")
    
    print("2. String Interning:")
    print("   Common strings stored once in memory")
    print("   Multiple variables can point to same string object")
    print("   Saves memory for frequently used strings")
    
    print("3. Immutability:")
    print("   Every operation creates new string objects")
    print("   Original strings never change")
    print("   join() is more efficient than repeated +")


def demonstrate_string_behavior():
    """Show string behavior and optimizations"""
    
    print("\n=== STRING BEHAVIOR ===")
    
    # String interning
    s1 = "hello"
    s2 = "hello"
    s3 = "he" + "llo"
    
    print("String Interning:")
    print(f"  s1 = 'hello'")
    print(f"  s2 = 'hello'")
    print(f"  s3 = 'he' + 'llo'")
    print(f"  s1 is s2: {s1 is s2} (same object)")
    print(f"  s1 is s3: {s1 is s3} (computed at runtime)")
    
    # Concatenation performance
    import time
    
    print("\nConcatenation Performance (5000 operations):")
    
    # Inefficient way
    start = time.time()
    result = ""
    for i in range(5000):
        result += str(i) + " "
    slow_time = time.time() - start
    
    # Efficient way
    start = time.time()
    parts = [str(i) for i in range(5000)]
    result = " ".join(parts)
    fast_time = time.time() - start
    
    print(f"  String concatenation (+): {slow_time:.4f}s")
    print(f"  String join():            {fast_time:.4f}s")
    if fast_time > 0:
        print(f"  join() is {slow_time/fast_time:.1f}x faster!")
    else:
        print("  join() is significantly faster than concatenation!")


# ============================================================================
# PRACTICAL GUIDELINES
# ============================================================================

def practical_guidelines():
    """Practical advice for choosing and using data structures"""
    
    print("\n" + "=" * 60)
    print("PRACTICAL GUIDELINES: WHEN TO USE WHAT")
    print("=" * 60)
    
    guidelines = {
        "📊 DICTIONARY": [
            "✅ When you need key-value mapping",
            "✅ When you need fast lookups by key",
            "✅ When you want to group/categorize data",
            "✅ When order matters (Python 3.7+)",
            "❌ Avoid if you only need to store single values"
        ],
        
        "📋 LIST": [
            "✅ When you need ordered, changeable data",
            "✅ When you frequently append items",
            "✅ When you need to access items by position",
            "✅ When you need to maintain duplicates",
            "❌ Avoid for frequent insertions in middle",
            "❌ Avoid for membership testing (use set instead)"
        ],
        
        "🔗 SET": [
            "✅ When you need unique items only",
            "✅ When you need fast membership testing",
            "✅ When you need set operations (union, intersection)",
            "✅ For removing duplicates from lists",
            "❌ Avoid when order matters",
            "❌ Avoid when you need to store unhashable items"
        ],
        
        "📦 TUPLE": [
            "✅ When data shouldn't change after creation",
            "✅ When you need to use as dictionary key",
            "✅ When you want to save memory",
            "✅ For coordinates, database records, etc.",
            "❌ Avoid when you need to modify contents"
        ],
        
        "📝 STRING": [
            "✅ Use join() for building strings from pieces",
            "✅ Use f-strings for formatting",
            "✅ Remember strings are immutable",
            "❌ Avoid repeated concatenation with +"
        ]
    }
    
    for structure, tips in guidelines.items():
        print(f"\n{structure}")
        for tip in tips:
            print(f"  {tip}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("PYTHON BUILT-IN DATA STRUCTURES: BEHIND THE SCENES")
    print("=" * 60)
    
    explain_dictionary_internals()
    demonstrate_dict_performance()
    
    explain_list_internals()
    demonstrate_list_performance()
    
    explain_set_internals()
    demonstrate_set_power()
    
    explain_tuple_internals()
    demonstrate_tuple_benefits()
    
    explain_sorting_internals()
    demonstrate_sorting_adaptiveness()
    
    explain_string_internals()
    demonstrate_string_behavior()
    
    practical_guidelines()
    
    print("\n" + "=" * 60)
    print("🎯 SUMMARY: CHOOSING THE RIGHT TOOL")
    print("=" * 60)
    print("""
    Remember: Each data structure is optimized for specific use cases.
    
    🚀 PERFORMANCE TIPS:
    • Use dict for fast key-based access
    • Use list for ordered data that changes
    • Use set for uniqueness and fast membership testing
    • Use tuple for immutable sequences
    • Use join() instead of + for string building
    
    💡 MEMORY TIPS:
    • Tuples use less memory than lists
    • Sets and dicts use more memory but provide speed
    • Strings are interned automatically when possible
    
    ⚡ SPEED TIPS:
    • Dictionary and set lookups are nearly instant
    • List append is fast, but insert in middle is slow
    • Sorting is very fast on partially sorted data
    • String operations create new objects
    """)
