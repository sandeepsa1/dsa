def DFS(graph, v, visited, stack):
    #print(v)
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            DFS(graph, u, visited, stack)
    stack.append(v)

def TopologicalSort(graph):
    stack = []
    visited = {v: False for v in graph}
    #print (visited)
    for v in graph:
        if not visited[v]:
            DFS(graph, v, visited, stack)
    return stack[::-1]  # Reverse the stack to get the topological ordering

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
print("Topological Ordering:", TopologicalSort(graph))