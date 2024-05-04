def prims_algorithm(graph):
    for u, v, w in graph:
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w            

    in_mst = [False] * V
    key_values = [float('inf')] * V
    parents = [-1] * V
    key_values[0] = 0

    for _ in range(V):
        u = min((v for v in range(V) if not in_mst[v]), key=lambda v: key_values[v])
        #print(u)

        in_mst[u] = True

        if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
            print(f"{vertices[parents[u]]} -- {vertices[u]} == {adj_matrix[u][parents[u]]}")

        for v in range(V):
            if 0 < adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                key_values[v] = adj_matrix[u][v]
                parents[v] = u

V = 4
adj_matrix = [[0] * V for _ in range(V)]
vertices = [j for j in range(V)]
graph = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

#print(adj_matrix)
#print(vertices)
print("Edges in the MST:")
prims_algorithm(graph)