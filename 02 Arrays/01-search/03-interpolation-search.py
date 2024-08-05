def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        pos = left + ((target - arr[left]) * (right - left) // (arr[right] - arr[left]))
        
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(interpolation_search(arr, target))
