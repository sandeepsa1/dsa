# Insert
print('Insert')
my_dict = {}
my_dict["name"] = "Alice"
print(my_dict)  # {'name': 'Alice'}

# Updating an existing key's value
my_dict["name"] = "Bob"
print(my_dict)  # {'name': 'Bob'}
print('\n')


# Update
print('Update')
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"age": 30, "city": "New York"})
print(my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print('\n')


# Delete
print('Delete')
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
del my_dict["age"]
print(my_dict)  # {'name': 'Alice', 'city': 'New York'}

removed_value = my_dict.pop("city")
print(removed_value)  # New York
print(my_dict)  # {'name': 'Alice'}

last_removed = my_dict.popitem()
print(last_removed)  # ('name', 'Alice')
print(my_dict)  # {}
print('\n')


# Check
print('Check')
# Check if a key exists
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)  # True
print("city" in my_dict)  # False

# Check if a value exists
print(25 in my_dict.values())  # True
print("New York" in my_dict.values())  # False

# Get a value safely using get()
print(my_dict.get("name"))  # Alice
print(my_dict.get("city", "Not Found"))  # Not Found