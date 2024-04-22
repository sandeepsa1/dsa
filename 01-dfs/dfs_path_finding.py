def dfs(graph, start, end, visited, path):
    visited[start] = True
    path.append(start)
    if start == end:
        return True  # Path found
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited, path):
                return True  # Path found
    path.pop()  # Backtrack
    return False  # Path not found

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
visited = {vertex: False for vertex in graph}
start_vertex = 'A'
end_vertex = 'G'
path = []

if dfs(graph, start_vertex, end_vertex, visited, path):
    print("Path found:", ' -> '.join(path))
else:
    print("No path found between", start_vertex, "and", end_vertex)
