def max_subarray_sum(arry):
    max_current = max_global = arry[0]
    start = end = s = 0

    for i in range(1, len(arry)):
        if arry[i] > max_current + arry[i]:
            max_current = arry[i]
            s = i
        else:
            max_current += arry[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i
    
    return max_global, arry[start:end+1]

arry = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum, subarray = max_subarray_sum(arry)
print("Maximum Subarray Sum:", max_sum)
print("Subarray:", subarray)