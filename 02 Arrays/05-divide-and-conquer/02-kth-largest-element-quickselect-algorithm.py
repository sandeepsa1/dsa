import random

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] > pivot:  # For k-th largest, use ">" (use "<" for k-th smallest)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    pivot_index = partition(arr, left, right)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

def find_kth_largest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k - 1)


arr = [3, 2, 1, 5, 6, 4]
k = 2
result = find_kth_largest(arr, k)
print(f"{k}-th largest element is {result}")