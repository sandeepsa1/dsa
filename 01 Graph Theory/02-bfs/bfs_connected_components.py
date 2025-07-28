graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D'],
    'F': [],
}

components = find_connected_components_bfs(graph)
print("Connected Components:", components)