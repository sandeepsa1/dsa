from collections import defaultdict

# Create an empty hash table (dictionary in Python)
hash_table = {}

hash_table["Alice"] = 85  # Insert
hash_table["Bob"] = 90    # Insert
hash_table["Alice"] = 95  # Update

print(hash_table)  # {'Alice': 95, 'Bob': 90}

del hash_table["Bob"]     # Delete

print(hash_table)  # {'Alice': 95}

# Trying to delete a key that doesn't exist will raise a KeyError
# del hash_table["Charlie"]  # Raises a KeyError: 'Charlie'

value = hash_table.get("Alice", "Not Found")    # Search
print(value)  # 95

value = hash_table.get("Charlie", "Not Found")
print(value)  # Not Found


# Collision handling
hash_table = defaultdict(list)

# Insert key-value pairs (simulate collision by using multiple values for same key)
hash_table[3].append(("Alice", 85))
hash_table[3].append(("Bob", 90))  # Collision handled by chaining

print(hash_table)  # {3: [('Alice', 85), ('Bob', 90)]}