dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4}

# Method 1: Using update()
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# Method 2: Using **
dict1 = {"a": 1, "b": 2, "c": 3}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# Method 3: Using |
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4}