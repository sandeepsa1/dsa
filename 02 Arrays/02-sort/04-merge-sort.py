def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res.extend(left[i:])
    res.extend(right[j:])

    return res

def merge_sort(arry):
    if len(arry) < 2:
        return arry

    mid = len(arry) // 2

    left = merge_sort(arry[:mid])
    right = merge_sort(arry[mid:])

    return merge(left, right)

arry = [7, 2, 5, 9, 4, 3, 6, 8, 1]
print(merge_sort(arry))