def length_of_lis(arr):
    if not arr:
        return []
    
    n = len(arr)
    sub = []
    indices = []
    prev_indices = [-1] * n

    for i, num in enumerate(arr):
        # Custom binary search to find the position to replace in sub
        low, high = 0, len(sub)
        while low < high:
            mid = (low + high) // 2
            if sub[mid] < num:
                low = mid + 1
            else:
                high = mid
        
        # If num is larger than all elements in sub, append it
        if low == len(sub):
            sub.append(num)
            indices.append(i)
        else:
            sub[low] = num
            indices[low] = i
        
        # Update the previous index of the current element
        if low > 0:
            prev_indices[i] = indices[low - 1]

    # Reconstruct the LIS
    lis = []
    k = indices[-1]
    while k >= 0:
        lis.append(arr[k])
        k = prev_indices[k]
    
    return lis[::-1]

arr = [10, 9, 2, 5, 3, 7, 101, 18]
lis = length_of_lis(arr)
print(f"Length of LIS: {len(lis)}")
print(f"LIS: {lis}")