def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]

def union(u, v, parent, rank):
    root_u = find(u, parent)
    root_v = find(v, parent)

    if root_u == root_v:
        return True

    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    elif rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return False

def hasCycle(graph, num_nodes):
    parent = list(range(num_nodes))
    rank = [1] * num_nodes

    for u, v in graph:
        if union(u, v, parent, rank):
            return True
    return False


graph = [
    (0, 1),
    (1, 2),
    (2, 0),
    (3, 4)
]

num_nodes = 5

if hasCycle(graph, num_nodes):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")