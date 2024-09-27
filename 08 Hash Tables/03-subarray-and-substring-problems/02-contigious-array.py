def findMaxLength(nums):
    prefix_sum_map = {}
    prefix_sum = 0
    max_length = 0

    prefix_sum_map[0] = -1

    for i in range(len(nums)):
        if nums[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[prefix_sum])
        else:
            prefix_sum_map[prefix_sum] = i

    return max_length


binary_array = [0, 1, 0, 1, 1, 1, 0, 0]
result = findMaxLength(binary_array)
print(result)  # 8 (entire array has equal number of 0s and 1s)