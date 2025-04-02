from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

def dfs_spanning_tree(graph, node, visited, spanning_tree):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            spanning_tree.append((node, neighbor))
            dfs_spanning_tree(graph, neighbor, visited, spanning_tree)

def get_spanning_tree(graph, start_node):
    visited = set()
    spanning_tree = []
    dfs_spanning_tree(graph, start_node, visited, spanning_tree)
    return spanning_tree


graph = defaultdict(list)
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]
for u, v in edges:
    add_edge(graph, u, v)

spanning_tree = get_spanning_tree(graph, 0)
print("DFS Spanning Tree edges:", spanning_tree) # [(0, 1), (1, 3), (1, 4), (4, 2)]