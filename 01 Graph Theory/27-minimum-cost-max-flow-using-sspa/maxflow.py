from collections import defaultdict
import math

def min_cost_max_flow(edges, source, sink):
    graph = defaultdict(dict)
    capacities = defaultdict(lambda: defaultdict(int))
    costs = defaultdict(lambda: defaultdict(int))
    
    for u, v, capacity, cost in edges:
        graph[u][v] = capacity
        graph[v][u] = 0
        capacities[u][v] = capacity
        costs[u][v] = cost
        costs[v][u] = -cost  # Reverse edge cost
    
    def bellman_ford():
        dist = {node: math.inf for node in graph}
        dist[source] = 0
        parent = {node: None for node in graph}
        
        for _ in range(len(graph) - 1):
            for u in graph:
                for v in graph[u]:
                    if capacities[u][v] > 0 and dist[u] + costs[u][v] < dist[v]:
                        dist[v] = dist[u] + costs[u][v]
                        parent[v] = u
                        
        return dist, parent
    
    def augment_flow(parent):
        flow = math.inf
        v = sink
        path = []
        
        while parent[v] is not None:
            u = parent[v]
            path.append((u, v))
            flow = min(flow, capacities[u][v])
            v = parent[v]
        
        path.reverse()
        v = sink
        while parent[v] is not None:
            u = parent[v]
            capacities[u][v] -= flow
            capacities[v][u] += flow
            v = parent[v]
        
        return flow, path
    
    total_flow = 0
    total_cost = 0
    paths = []

    while True:
        dist, parent = bellman_ford()
        if dist[sink] == math.inf:
            break
        
        flow, path = augment_flow(parent)
        total_flow += flow
        total_cost += flow * dist[sink]
        paths.append((path, flow, dist[sink]))
    
    return total_flow, total_cost, paths


edges = [
    ('S', 'A', 10, 2), ('S', 'C', 10, 3),
    ('A', 'B', 4, 3), ('A', 'C', 2, 1),
    ('A', 'D', 8, 1), ('C', 'D', 9, 2),
    ('D', 'B', 6, 4), ('B', 'T', 10, 4),
    ('D', 'T', 10, 1)
]

source = 'S'
sink = 'T'

flow, cost, paths = min_cost_max_flow(edges, source, sink)
print(f"Minimum Cost: {cost}")
print(f"Maximum Flow: {flow}")

print("Paths and Flow:")
for path, flow, path_cost in paths:
    path_str = " -> ".join([f"{u}({flow}:{flow})" for u, v in path] + [sink])
    print(f"Path: {path_str}")
    print(f"Flow: {flow}")
    print(f"Path Cost: {path_cost}")