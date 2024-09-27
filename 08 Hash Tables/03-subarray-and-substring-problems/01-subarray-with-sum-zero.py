def has_subarray_with_zero_sum(arr):
    sum_set = set()
    
    cum_sum = 0
    
    for num in arr:
        cum_sum += num
        
        if cum_sum == 0 or cum_sum in sum_set:
            return True
        
        sum_set.add(cum_sum)
    
    return False


arr = [4, 2, -3, 1, 6]
result = has_subarray_with_zero_sum(arr)
print(result)  # True (because the subarray [2, -3, 1] has a sum of 0)