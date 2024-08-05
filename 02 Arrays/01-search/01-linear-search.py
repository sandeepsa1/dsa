def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [4, 2, 3, 1, 5]
target = 3
print(linear_search(arr, target))