from collections import defaultdict

def edge_list_to_adj_list(edge_list, n):
    adj_list = defaultdict(list)
    for u, v in edge_list:
        adj_list[u].append(v)
        adj_list[v].append(u)  # For undirected graphs, include this line
    return dict(adj_list)


edge_list = [(0, 1), (1, 2), (1, 3)]
print(edge_list_to_adj_list(edge_list, 4)) # {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}