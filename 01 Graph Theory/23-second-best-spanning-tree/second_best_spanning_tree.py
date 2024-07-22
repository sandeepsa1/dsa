def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(n, edges):
    parent = list(range(n)) # [0, 1, 2, 3]
    rank = [0] * n # [0, 0, 0, 0]
    
    edges.sort(key=lambda edge: edge[2])
    
    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost

def second_best_spanning_tree(n, edges):
    
    mst, mst_cost = kruskal(n, edges)
    second_best_cost = float('inf')
    second_best_mst = None

    for i in range(len(mst)):
        candidate_edges = edges.copy()
        mst_edge = mst[i]
        candidate_edges.remove(mst_edge)
        
        # Find the MST of the modified graph
        parent = list(range(n))
        rank = [0] * n
        candidate_tree = []
        total_weight = 0
        
        for u, v, weight in candidate_edges:
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                candidate_tree.append((u, v, weight))
                total_weight += weight
                if len(candidate_tree) == n - 1:
                    break

        if len(candidate_tree) == n - 1 and total_weight < second_best_cost and total_weight > mst_cost:
            second_best_cost = total_weight
            second_best_mst = candidate_tree

    return second_best_cost, second_best_mst

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4

mst, mst_cost = kruskal(n, edges)
print(f"Minimum Spanning Tree: {mst}")
print(f"Cost of Minimum Spanning Tree: {mst_cost}")

second_best_cost, second_best_mst = second_best_spanning_tree(n, edges)
print(f"Second best MST: {second_best_mst}")
print(f"Cost of Second best MST: {second_best_cost}")