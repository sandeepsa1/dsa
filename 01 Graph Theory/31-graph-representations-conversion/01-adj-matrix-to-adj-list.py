def adj_matrix_to_adj_list(adj_matrix):
    n = len(adj_matrix)
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:
                adj_list[i].append(j)
    return adj_list


adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
print(adj_matrix_to_adj_list(adj_matrix)) # [[1], [0, 2, 3], [1], [1]] 