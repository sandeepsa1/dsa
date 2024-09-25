def count_frequencies(collection):
    frequency_table = {}

    for item in collection:
        if item in frequency_table:
            frequency_table[item] += 1
        else:
            frequency_table[item] = 1

    return frequency_table


collection = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

frequency = count_frequencies(collection)

print(frequency)  # {'apple': 3, 'banana': 2, 'orange': 1}