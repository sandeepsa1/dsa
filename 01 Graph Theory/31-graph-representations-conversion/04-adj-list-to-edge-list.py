def adj_list_to_edge_list(adj_list):
    edge_list = []
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            edge_list.append((i, neighbor))
    return edge_list


adj_list = [[1], [0, 2, 3], [1], [1]]
print(adj_list_to_edge_list(adj_list)) # [(0, 1), (1, 0), (1, 2), (1, 3), (2, 1), (3, 1)]