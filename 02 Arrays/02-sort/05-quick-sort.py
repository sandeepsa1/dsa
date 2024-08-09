def quick_sort(arry):
    n = len(arry)
    if(n < 2):
        return arry
    else:
        pivot = arry[n // 2]
        left = [x for x in arry if x < pivot]
        mid = [x for x in arry if x == pivot]
        right = [x for x in arry if x > pivot]

        return quick_sort(left) + mid + quick_sort(right)

arry = [7, 2, 5, 9, 4, 3, 6, 8, 1]
print(quick_sort(arry))