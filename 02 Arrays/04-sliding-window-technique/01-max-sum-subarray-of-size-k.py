def max_sum_subarray_of_size_k(arr, k):
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray_of_size_k(arr, k)
print(f"The maximum sum of a subarray of size {k} is {result}.")