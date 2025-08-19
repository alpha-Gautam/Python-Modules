"""
PYTHON BUILT-IN DATA STRUCTURES: COMPLETE GUIDE
===============================================

This comprehensive guide explains how Python's core data structures work internally,
what algorithms they use "behind the scenes," and when to use each one.

SUMMARY OF ALL FILES CREATED:
1. python_data_structures_explained.py - Main educational overview with examples
2. python_data_structures_deep_dive.py - Advanced implementation details
3. python_data_structures_internals_fixed.py - Low-level internal workings

============================================
🎯 QUICK REFERENCE: WHAT TO USE WHEN
============================================

📚 DICTIONARY (dict) - Hash Table
WHEN TO USE:
✅ Key-value mapping (name → phone number)
✅ Fast lookups by unique identifier
✅ Counting/grouping (word frequencies)
✅ Caching computed results
✅ When order matters (Python 3.7+)

BEHIND THE SCENES:
• Uses sophisticated hash table with open addressing
• Maintains insertion order since Python 3.7
• Compact memory layout saves 20-25% memory vs old implementation
• O(1) average case for lookup, insert, delete
• Handles hash collisions with pseudo-random probing

EXAMPLE:
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
# Instant lookup: scores['Alice'] → 95

-------------------------------------------

📋 LIST - Dynamic Array
WHEN TO USE:
✅ Ordered, changeable sequences
✅ Frequent appending to end
✅ Access by position/index
✅ Stack operations (append/pop)
✅ When duplicates are allowed

BEHIND THE SCENES:
• Dynamic array that over-allocates memory
• Growth strategy: ~12.5% extra space when full
• Stores pointers to objects, not objects themselves
• O(1) append (amortized), O(1) access, O(n) insert in middle
• Memory layout: [header][ptr1][ptr2]...[unused slots]

EXAMPLE:
tasks = ['email', 'meeting', 'code review']
tasks.append('lunch')  # Very fast
tasks.insert(0, 'standup')  # Slower - must shift everything

-------------------------------------------

🔗 SET - Hash Table for Uniqueness  
WHEN TO USE:
✅ Unique items only
✅ Fast membership testing ("is X in the collection?")
✅ Mathematical set operations (union, intersection)
✅ Removing duplicates from lists
✅ When order doesn't matter

BEHIND THE SCENES:
• Hash table like dict but simpler (keys only, no values)
• Same collision resolution as dictionaries
• Set operations optimized to iterate through smaller set
• O(1) average case for add, remove, contains
• Items must be hashable (immutable)

EXAMPLE:
seen_users = set()
if user_id not in seen_users:  # Very fast check
    seen_users.add(user_id)
    process_new_user(user_id)

-------------------------------------------

📦 TUPLE - Immutable Sequence
WHEN TO USE:
✅ Data that shouldn't change after creation
✅ Dictionary keys (if contents are hashable)
✅ Multiple return values from functions
✅ Coordinates, database records
✅ When memory efficiency matters

BEHIND THE SCENES:
• Fixed-size array of object pointers
• More memory efficient than lists (no over-allocation)
• Small tuples are cached and reused by Python
• Hashable if all contents are hashable
• Cannot be modified after creation

EXAMPLE:
point = (3, 4)  # Coordinate
locations = {(0, 0): 'origin', (3, 4): 'point A'}  # Dict key
x, y = point  # Unpacking

-------------------------------------------

🔤 STRING - Immutable Unicode Sequence
WHEN TO USE:
✅ Text processing and manipulation
✅ When using join() for building from parts
✅ Template formatting with f-strings
✅ When immutability is desired

BEHIND THE SCENES:
• Variable-width Unicode encoding (1-4 bytes per character)
• String interning for common strings saves memory
• Immutable - every operation creates new string
• join() much faster than repeated + concatenation
• Optimized for various encodings (ASCII, Latin-1, Unicode)

EXAMPLE:
# Efficient string building
parts = ['Hello', 'beautiful', 'world']
message = ' '.join(parts)  # Much faster than += loop

============================================
⚡ SORTING: TIMSORT ALGORITHM
============================================

WHAT IT IS:
Python's built-in sorting algorithm, used by sorted() and list.sort()

BEHIND THE SCENES:
• Hybrid algorithm: insertion sort + merge sort
• Adaptive: runs faster on partially sorted data
• Stable: equal items keep their relative order
• Finds existing sorted "runs" and merges them efficiently
• Galloping mode for data with patterns

PERFORMANCE:
• Best case: O(n) - already sorted data
• Average case: O(n log n) 
• Worst case: O(n log n)
• Real-world data often performs much better than worst case

WHY IT'S SPECIAL:
✅ Optimized for real-world data patterns
✅ Maintains stable sort order
✅ Adaptive performance based on existing order

============================================
📊 PERFORMANCE COMPARISON
============================================

OPERATION              | LIST   | SET    | DICT   | TUPLE
--------------------- |--------|--------|--------|--------
Access by index       | O(1)   | N/A    | N/A    | O(1)
Access by key          | N/A    | N/A    | O(1)   | N/A
Search for value       | O(n)   | O(1)   | O(n)   | O(n)
Insert at end          | O(1)*  | O(1)   | O(1)   | N/A
Insert in middle       | O(n)   | O(1)   | O(1)   | N/A
Delete                 | O(n)   | O(1)   | O(1)   | N/A
Memory usage           | Medium | High   | High   | Low

* Amortized O(1) due to over-allocation

============================================
🧠 MEMORY USAGE INSIGHTS
============================================

For 1000 integers:
• String of digits: ~1,041 bytes (most efficient)
• Tuple: ~8,040 bytes  
• List: ~8,056 bytes
• Set: ~32,984 bytes (hash table overhead)
• Dict: ~36,952 bytes (highest overhead)

MEMORY TIPS:
💡 Use tuples for read-only data
💡 Use sets/dicts only when you need their special capabilities
💡 String operations create new objects - use join() for efficiency

============================================
🎓 PRACTICAL GUIDELINES
============================================

CHOOSING THE RIGHT DATA STRUCTURE:

1. Need fast key-based lookup? → DICTIONARY
   scores = {'Alice': 95, 'Bob': 87}

2. Need ordered, changeable data? → LIST  
   tasks = ['email', 'meeting', 'lunch']

3. Need uniqueness and fast "contains" check? → SET
   processed_ids = {1, 5, 9, 12}

4. Need immutable sequence? → TUPLE
   coordinates = (10, 20)

5. Building strings from parts? → JOIN
   result = ' '.join(word_list)

COMMON ANTI-PATTERNS TO AVOID:
❌ Using list for membership testing (use set)
❌ Using + for building long strings (use join)
❌ Using dict when you only need values (use set)
❌ Frequent insertions in middle of list (use deque)

============================================
🚀 REAL-WORLD PERFORMANCE TIPS
============================================

1. DICTIONARY LOOKUPS:
   # Instead of linear search in list
   for user in user_list:
       if user.id == target_id:
           return user
   
   # Use dictionary for instant lookup
   user = user_dict[target_id]

2. SET OPERATIONS:
   # Remove duplicates efficiently
   unique_items = list(set(item_list))
   
   # Fast intersection
   common = set1 & set2

3. STRING BUILDING:
   # Slow way
   result = ""
   for word in words:
       result += word + " "
   
   # Fast way
   result = " ".join(words)

4. LIST OPERATIONS:
   # Use list comprehensions when possible
   squares = [x**2 for x in numbers]
   
   # Use append() instead of insert(0, item)
   items.append(new_item)  # O(1)
   # NOT: items.insert(0, new_item)  # O(n)

============================================
🎯 FINAL SUMMARY
============================================

Python's built-in data structures are highly optimized and well-designed:

🔹 DICTIONARIES use sophisticated hash tables with order preservation
🔹 LISTS use dynamic arrays with smart memory allocation  
🔹 SETS use hash tables optimized for uniqueness and membership testing
🔹 TUPLES use immutable arrays with memory optimization
🔹 SORTING uses the adaptive Timsort algorithm
🔹 STRINGS use variable-width Unicode with interning

The key to writing efficient Python code is understanding when to use each 
data structure and leveraging their strengths for your specific use case.

Remember: Python prioritizes developer productivity while maintaining 
performance through clever implementation details that work behind the scenes.
"""
