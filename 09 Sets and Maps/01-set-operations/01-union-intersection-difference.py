# Union
print('Union')
A = {1, 2, 3}
B = {3, 4, 5}

# Using union() method
result1 = A.union(B)
print(result1)  # {1, 2, 3, 4, 5}

# Using '|' operator
result2 = A | B
print(result2)  # {1, 2, 3, 4, 5}
print('\n')


# Intersection
print('Intersection')
A = {1, 2, 3}
B = {3, 4, 5}

# Using intersection() method
result1 = A.intersection(B)
print(result1)  # {3}

# Using '&' operator
result2 = A & B
print(result2)  # {3}
print('\n')


# Difference
print('Difference')
A = {1, 2, 3}
B = {3, 4, 5}

# Elements in A but not in B
result1 = A.difference(B)
print(result1)  # {1, 2}

# Using '-' operator
result2 = A - B
print(result2)  # {1, 2}

# Elements in B but not in A
result3 = B - A
print(result3)  # {4, 5}