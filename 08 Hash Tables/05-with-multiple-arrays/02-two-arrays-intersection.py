def intersect(arr1, arr2):
    count_map = {}
    for num in arr1:
        count_map[num] = count_map.get(num, 0) + 1
    
    result = []
    for num in arr2:
        if num in count_map and count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1
    
    return result


arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersect(arr1, arr2))  # [2, 2]

arr1 = [4, 9, 5]
arr2 = [9, 4, 9, 8, 4]
print(intersect(arr1, arr2))  # [4, 9]