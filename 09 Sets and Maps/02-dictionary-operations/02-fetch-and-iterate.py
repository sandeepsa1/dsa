my_dict = {"name": "Alice", "age": 25, "city": "New York", "profession": "Engineer"}

# Get Value by Key
print(my_dict.get("name"))                # Alice
print(my_dict.get("country", "Unknown"))  # Unknown

# Iterate over keys
print("\nKeys:")
for key in my_dict:
    print(key)

# Iterate over values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")