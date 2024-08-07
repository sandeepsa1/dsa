def selection_sort(arry):
    n = len(arry)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if(arry[j] < arry[min_idx]):
                min_idx = j
        
        arry[i], arry[min_idx] = arry[min_idx], arry[i]

    return arry

arry = [7, 2, 5, 9, 4, 3, 6, 8, 1]
print(selection_sort(arry))