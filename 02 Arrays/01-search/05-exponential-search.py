def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    
    index = 1
    while index < n and arr[index] <= target:
        index *= 2
    
    return binary_search(arr, target, index // 2, min(index, n-1))

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(exponential_search(arr, target))