def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        all_sorted = True

        for j in range(n - i - 1):
            if(arry[j] > arry[j + 1]):
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
                all_sorted = False
        
        if all_sorted:
            break

    return arry

arry = [7, 2, 5, 9, 4, 3, 6, 8, 1]
print(bubble_sort(arry))