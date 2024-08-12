import random

def partition(arry, left, right):
    pivot = arry[right]
    i = left
    for j in range(left, right):
        if arry[j] > pivot:  # For k-th largest, use ">" (use "<" for k-th smallest)
            arry[i], arry[j] = arry[j], arry[i]
            i += 1
    arry[i], arry[right] = arry[right], arry[i]
    return i

def quickselect(arry, left, right, k):
    if left == right:
        return arry[left]
    
    pivot_index = random.randint(left, right)
    arry[pivot_index], arry[right] = arry[right], arry[pivot_index]
    
    pivot_index = partition(arry, left, right)
    
    if k == pivot_index:
        return arry[k]
    elif k < pivot_index:
        return quickselect(arry, left, pivot_index - 1, k)
    else:
        return quickselect(arry, pivot_index + 1, right, k)

def find_kth_largest(arry, k):
    return quickselect(arry, 0, len(arry) - 1, k - 1)


arry = [3, 2, 1, 5, 6, 4]
k = 2
result = find_kth_largest(arry, k)
print(f"{k}-th largest element is {result}")