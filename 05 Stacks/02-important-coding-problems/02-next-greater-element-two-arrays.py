def next_greater_element(nums1, nums2):
    nge_map = {}
    stack = []

    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        
        nge_map[num] = stack[-1] if stack else -1
        
        stack.append(num)

    result = [nge_map.get(num, -1) for num in nums1]

    return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = next_greater_element(nums1, nums2)
print(result)  # [-1, 3, -1]