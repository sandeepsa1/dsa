def insertion_sort(arry):
    n = len(arry)

    for i in range(1, n):
        key = arry[i]
        
        j = i - 1
        while j >= 0 and arry[j] > key:
            arry[j + 1] = arry[j]
            j -= 1
        
        arry[j + 1] = key
    
    return arry

arry = [7, 2, 5, 9, 4, 3, 6, 8, 1]
print(insertion_sort(arry))