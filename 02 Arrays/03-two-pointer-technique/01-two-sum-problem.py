def find_two_sum(arry, target):
    num_map = {}

    for i, num in enumerate(arry):
        complement = target - num
        # print(complement, num_map, complement in num_map)
        
        if complement in num_map:
            return num_map[complement], i
        
        num_map[num] = i

    return None

arry = [2, 7, 11, 15, 19]
target = 9
result = find_two_sum(arry, target)
if result:
    print(f"Indices of the two numbers that sum up to {target} are: {result}")
else:
    print("No two numbers found that sum up to the target.")