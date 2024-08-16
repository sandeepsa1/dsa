def rotate_matrix(matrix, degrees):
    n = len(matrix)
    
    if degrees == 90 or degrees == 270: # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    if degrees == 90 or degrees == 180: # Reverse each row
        for i in range(n):
            matrix[i].reverse()
    
    if degrees == 270: # Reverse each column
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

    if degrees == 180: # Reverse the order of the rows
        matrix.reverse()
    
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix(matrix, 90) # 180, 270
for row in rotated_matrix:
    print(row)