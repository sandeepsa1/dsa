def adj_matrix_to_edge_list(adj_matrix):
    edge_list = []
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i, n):
            if adj_matrix[i][j] != 0:
                edge_list.append((i, j))
    return edge_list


adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
print(adj_matrix_to_edge_list(adj_matrix)) # [(0, 1), (1, 2), (1, 3)]