def edge_list_to_adj_matrix(edge_list, n):
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edge_list:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1  # For undirected graphs
    return adj_matrix


edge_list = [(0, 1), (1, 2), (1, 3)]
print(edge_list_to_adj_matrix(edge_list, 4)) # [0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]] 