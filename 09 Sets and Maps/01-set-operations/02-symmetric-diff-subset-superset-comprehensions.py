# Symmetric Difference of Sets
print('Symmetric Difference of Sets')
A = {1, 2, 3}
B = {1, 2, 3}

result = A ^ B
print(result) # set()
print('\n')


# Subset Check
print('Subset Check')
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

result = A.issubset(B)
print(result)  # True

# Using operator
print(A <= B)  # True
print('\n')


# Superset Check
print('Superset Check')
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

result = A.issuperset(B)
print(result)  # True

# Using operator
print(A >= B)  # True
print('\n')


# Set Comprehensions
print('Set Comprehensions')
numbers = [1, 2, 3, 4, 5]                           # Squaring
squares = {x**2 for x in numbers}
print(squares)  # {1, 4, 9, 16, 25}

numbers = [1, 2, 3, 4, 5, 6, 7, 8]                  # Filter
evens = {x for x in numbers if x % 2 == 0}
print(evens)  # {2, 4, 6, 8}

nums = [1, 2, 2, 3, 4, 4, 5]                        # Duplicate Removal
unique_nums = {x for x in nums}
print(unique_nums)  # {1, 2, 3, 4, 5}

text = "hello world"                                # Extract Vowels
vowels = {char for char in text if char in 'aeiou'}
print(vowels)  # {'o', 'e'}

A = {1, 2}                                          # Cartesian Product
B = {3, 4}
pairs = {(a, b) for a in A for b in B}
print(pairs)  # {(1, 3), (1, 4), (2, 3), (2, 4)}