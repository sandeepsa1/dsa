def max_sum_subarray_of_size_k(arry, k):
    max_sum = sum(arry[:k])
    current_sum = max_sum
    
    for i in range(k, len(arry)):
        current_sum += arry[i] - arry[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arry = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray_of_size_k(arry, k)
print(f"The maximum sum of a subarray of size {k} is {result}.")