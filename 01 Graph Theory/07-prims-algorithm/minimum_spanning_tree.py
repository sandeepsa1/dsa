import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    mst = []
    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, vertex, parent) tuple

    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += weight

        if parent != -1:
            mst.append((parent, u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4

mst, total_cost = prim(n, edges)
print(f"Minimum Spanning Tree: {mst}")
print(f"Cost of Minimum Spanning Tree: {total_cost}")