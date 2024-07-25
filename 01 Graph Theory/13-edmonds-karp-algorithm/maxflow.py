from collections import deque, defaultdict

def bfs(residual_graph, source, sink, parent):
    visited = {v: False for v in residual_graph}
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in residual_graph[u]:
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph_edges, source, sink):
    
    residual_graph = defaultdict(list)
    for u, v, capacity in graph_edges:
        residual_graph[u].append([v, capacity])
        residual_graph[v].append([u, 0])  # Add reverse edge with 0 capacity
    
    
    parent = {}
    max_flow = 0
    
    # Augment the flow while there is a path from source to sink
    while bfs(residual_graph, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        while s != source:
            u = parent[s]
            for v, capacity in residual_graph[u]:
                if v == s:
                    path_flow = min(path_flow, capacity)
            s = parent[s]

        # update residual capacities of the edges and reverse edges along the path
        v = sink
        while v != source:
            u = parent[v]
            for edge in residual_graph[u]:
                if edge[0] == v:
                    edge[1] -= path_flow
            for edge in residual_graph[v]:
                if edge[0] == u:
                    edge[1] += path_flow
            v = parent[v]

        max_flow += path_flow
    
    return max_flow

edges = [
    ('S', 'A', 10), ('S', 'C', 10),
    ('A', 'B', 4), ('A', 'C', 2),
    ('A', 'D', 8), ('C', 'D', 9),
    ('D', 'B', 6), ('B', 'T', 10),
    ('D', 'T', 10)
]

source = 'S'
sink = 'T'

max_flow = edmonds_karp(edges, source, sink)
print(f"The maximum possible flow is {max_flow}")