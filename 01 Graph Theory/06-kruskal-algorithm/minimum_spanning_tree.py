def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): # To find if the new edge forms a cycle
    x_root = find(parent, x)
    y_root = find(parent, y)
    # print((x_root, y_root))

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(n, graph):
    parent = list(range(n)) # [0, 1, 2, 3]
    rank = [0] * n # [0, 0, 0, 0]
    
    graph.sort(key=lambda edge: edge[2])
    
    mst = []
    mst_cost = 0

    for u, v, weight in graph:
        # print(parent)
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost

n = 4
graph = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst, mst_cost = kruskal(n, graph)
print(f"Minimum Spanning Tree: {mst}")
print(f"Cost of Minimum Spanning Tree: {mst_cost}")
