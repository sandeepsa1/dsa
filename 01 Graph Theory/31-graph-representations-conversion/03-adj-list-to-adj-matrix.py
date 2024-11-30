def adj_list_to_adj_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = 1
    return adj_matrix


adj_list = [[1], [0, 2, 3], [1], [1]]
print(adj_list_to_adj_matrix(adj_list)) # [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]