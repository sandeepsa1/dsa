def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    # Left pass
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
        #print(answer, left_product)
    
    # Right pass
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
        #print(answer, right_product)
    
    return answer


nums = [1, 2, 3, 4]
# nums = [4, 3, 2, 1, 2]
print(product_except_self(nums))