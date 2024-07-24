def topological_sort(graph):
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)
    
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)
    
    return stack[::-1]  # Return the stack in reverse order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'P': ['Q', 'R'], # Disconnected
    'Q': ['S'],
    'R': ['T']
}
print("Topological Ordering:", topological_sort(graph))
