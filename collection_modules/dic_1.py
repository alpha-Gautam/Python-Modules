"""
This Python file demonstrates common dictionary operations along with their
average and worst-case time complexities in Big O notation.

Notes on Time Complexity:
- 'n' represents the number of key-value pairs (elements) in the dictionary.
- Average Case: Assumes a good hash function and minimal hash collisions.
- Worst Case: Can occur with poor hash functions or adversarial inputs leading to
  many hash collisions, potentially degrading performance.
"""

import operator

def demonstrate_dictionary_operations():
    """
    Demonstrates various dictionary operations and their time complexities.
    """

    print("--- Dictionary Operations and Time Complexities ---")

    # 1. Creation and Initialization
    # -----------------------------

    # Empty dictionary:
    my_dict = {}  # Time Complexity: O(1)
    print(f"\n1. Creation: Empty dictionary: {my_dict}")

    # With initial key-value pairs:
    my_dict = {'apple': 10, 'banana': 25, 'orange': 15, 'grape': 30}
    # Time Complexity: O(n) where 'n' is the number of initial pairs
    print(f"   Creation: Initialized dictionary: {my_dict}")

    # Using dict() constructor from a list of tuples:
    my_dict_from_tuples = dict([('key1', 'value1'), ('key2', 'value2')])
    # Time Complexity: O(n) where 'n' is the number of tuples
    print(f"   Creation: From list of tuples: {my_dict_from_tuples}")

    # Using dict.fromkeys():
    keys = ['key_a', 'key_b', 'key_c']
    default_value = 0
    my_dict_from_keys = dict.fromkeys(keys, default_value)
    # Time Complexity: O(len(keys))
    print(f"   Creation: Using fromkeys: {my_dict_from_keys}")

    # 2. Accessing Elements
    # --------------------

    print("\n2. Accessing Elements:")
    # Using square brackets []:
    value_apple = my_dict['apple']
    # Time Complexity: Average O(1), Worst Case O(n) due to collisions
    print(f"   Access 'apple' using []: {value_apple}")

    # Using the get() method:
    value_banana = my_dict.get('banana', 'Not Found')
    # Time Complexity: Average O(1), Worst Case O(n) due to collisions
    value_kiwi = my_dict.get('kiwi', 'Default Value')
    print(f"   Access 'banana' using get(): {value_banana}")
    print(f"   Access 'kiwi' (not found) using get(): {value_kiwi}")

    # 3. Adding and Modifying Elements
    # -------------------------------

    print("\n3. Adding and Modifying Elements:")
    # Adding a new key-value pair:
    my_dict['grape'] = 30  # Time Complexity: Average O(1), Worst Case O(n)
    print(f"   Added 'grape': {my_dict}")

    # Modifying an existing value:
    my_dict['apple'] = 12  # Time Complexity: Average O(1), Worst Case O(n)
    print(f"   Modified 'apple': {my_dict}")

    # Using the update() method:
    another_dict = {'cherry': 40, 'apple': 14}
    my_dict.update(another_dict)
    # Time Complexity: O(k) where 'k' is the number of items in the 'other_dict'
    print(f"   Updated with another dictionary: {my_dict}")

    # Using setdefault():
    value_existing = my_dict.setdefault('cherry', 50)
    value_new = my_dict.setdefault('lemon', 20)
    # Time Complexity: Average O(1), Worst Case O(n)
    print(f"   setdefault 'cherry' (exists): {value_existing}, Dict: {my_dict}")
    print(f"   setdefault 'lemon' (new): {value_new}, Dict: {my_dict}")

    # 4. Deleting Elements
    # -------------------

    print("\n4. Deleting Elements:")
    # Using the del statement:
    del my_dict['banana']  # Time Complexity: Average O(1), Worst Case O(n)
    print(f"   Deleted 'banana' using del: {my_dict}")

    # Using the pop() method:
    removed_value = my_dict.pop('orange')
    # Time Complexity: Average O(1), Worst Case O(n)
    print(f"   Popped 'orange': {removed_value}, Dict: {my_dict}")

    # Using the popitem() method:
    removed_key, removed_value = my_dict.popitem()
    # Time Complexity: Average O(1)
    print(f"   Popped random item: {removed_key}: {removed_value}, Dict: {my_dict}")

    # Using the clear() method:
    my_dict.clear()  # Time Complexity: O(1)
    print(f"   Cleared dictionary: {my_dict}")

    # 5. Iterating Through Dictionaries
    # --------------------------------

    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    print("\n5. Iterating Through Dictionaries:")

    # Iterating through keys:
    print("   Keys:")
    for key in my_dict:  # Time Complexity: O(n)
        print(f"     - {key}")

    # Iterating through values:
    print("   Values:")
    for value in my_dict.values():  # Time Complexity: O(n)
        print(f"     - {value}")

    # Iterating through key-value pairs:
    print("   Key-Value Pairs:")
    for key, value in my_dict.items():  # Time Complexity: O(n)
        print(f"     - {key}: {value}")

    # 6. Other Useful Operations
    # --------------------------

    print("\n6. Other Useful Operations:")

    # Checking for key existence:
    if 'key2' in my_dict:  # Time Complexity: Average O(1), Worst Case O(n)
        print("   'key2' exists in dictionary.")

    # Getting the length of the dictionary:
    length = len(my_dict)  # Time Complexity: O(1)
    print(f"   Length of dictionary: {length}")

    # Copying a dictionary:
    new_dict = my_dict.copy()  # Time Complexity: O(n)
    print(f"   Copied dictionary: {new_dict}")

    # Finding the maximum value in the dictionary (refer to previous examples)
    my_numeric_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
    max_val = max(my_numeric_dict.values()) # Time Complexity: O(n)
    print(f"   Max value in numeric dictionary: {max_val}")

    max_item = max(my_numeric_dict.items(), key=operator.itemgetter(1)) # Time Complexity: O(n)
    print(f"   Key and value of max item: {max_item}")

    # 7. Dictionary Comprehension
    # ---------------------------

    print("\n7. Dictionary Comprehension:")

    # Creating a new dictionary from a list, using list comprehension
    list_numbers = [1, 2, 3, 4]
    squared_dict = {num: num**2 for num in list_numbers}
    # Time Complexity: O(len(list_numbers))
    print(f"   Squared dictionary from list: {squared_dict}")

    # Filtering and transforming based on existing dictionary:
    filtered_dict = {k: v * 2 for k, v in squared_dict.items() if v % 2 == 0}
    # Time Complexity: O(len(squared_dict))
    print(f"   Filtered and transformed dictionary: {filtered_dict}")


if __name__ == "__main__":
    # demonstrate_dictionary_operations()
    
    my_numeric_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
    max_val = max(my_numeric_dict.values()) # Time Complexity: O(n)
    values=(my_numeric_dict.values()) # Time Complexity: O(n)
    # print(f"   Max value in numeric dictionary: {max_val}")
    print(f"   Values in numeric dictionary: {values}")
    for i in values:
        print(i)

    pass
