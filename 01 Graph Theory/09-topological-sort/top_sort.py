from collections import defaultdict

def top_sort(v, visited, stack, graph):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            top_sort(neighbor, visited, stack, graph)

    stack.insert(0, v)

def topological_sort(graph):
    visited = {key: False for key in graph}
    stack = []

    for vertex in graph:
        if not visited[vertex]:
            top_sort(vertex, visited, stack, graph)

    return stack

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("Topological Sort of the given graph:")
result = topological_sort(graph)
print(result)