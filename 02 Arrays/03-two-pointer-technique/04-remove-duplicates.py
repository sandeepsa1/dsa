def remove_duplicates(arry):
    arry.sort()
    unique_index = 0
    
    for i in range(1, len(arry)):
        if arry[i] != arry[unique_index]:
            unique_index += 1
            arry[unique_index] = arry[i]
    
    return unique_index + 1

arry = [1, 2, 3, 3, 4, 1, 3, 4, 2, 5]
new_length = remove_duplicates(arry)
print("Array with duplicates removed:", arry[:new_length])
print("New length of the array:", new_length)