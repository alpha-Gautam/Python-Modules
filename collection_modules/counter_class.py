from collections import Counter

# Example 1: Counting characters in a string
text = "banana"
count = Counter(text)
print(count)  # Output: Counter({'a': 3, 'n': 2, 'b': 1})

# Example 2: Counting elements in a list
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
print(count)  # Output: Counter({3: 3, 2: 2, 1: 1})


print(count[3])  # Get count of 3


print(count.most_common(2))  # [(3, 3), (2, 2)]


count.update([3, 3, 4])
print(count)  # Counter({3: 5, 2: 2, 1: 1, 4: 1})


count.subtract([3, 2])
print(count)  # Counter({3: 4, 2: 1, 1: 1, 4: 1})





# You can implement a simple counter manually using a dictionary:
def m_counter(iterable):
    count_dict = {}
    for item in iterable:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Example
print(m_counter("banana"))  # {'b': 1, 'a': 3, 'n': 2}
