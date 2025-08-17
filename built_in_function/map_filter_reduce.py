from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Step 1: Square each number
squares = map(lambda x: x**2, nums)   # [1, 4, 9, 16, 25, 36]

# Step 2: Keep only even squares
evens = filter(lambda x: x % 2 == 0, squares)  # [4, 16, 36]

# Step 3: Find the sum of remaining values
result = reduce(lambda x, y: x + y, evens)     # 56

print(result)
