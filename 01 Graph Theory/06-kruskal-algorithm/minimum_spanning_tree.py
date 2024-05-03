def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): # To find if the new edge forms a cycle
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(V, graph):
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    #print(graph)
    parent = [j for j in range(V)] # [0, 1, 2, 3]
    rank = [0] * V  # [0, 0, 0, 0]

    while e < V - 1:
        u, v, w = graph[i]
        #print([u, v, w])
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        print([u, v, x, y])

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    print("Edges in the MST:")
    for u, v, weight in result:
        print(f"{u} -- {v} == {weight}")

V = 4
graph = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

kruskal(V, graph)