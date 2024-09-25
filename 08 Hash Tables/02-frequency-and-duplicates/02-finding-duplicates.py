def find_duplicates(arr):
    seen = {}
    duplicates = []

    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen[item] = 1

    return duplicates


arr = [1, 2, 3, 4, 5, 3, 2, 6, 1]

duplicates = find_duplicates(arr)

print(duplicates)  # [3, 2, 1]