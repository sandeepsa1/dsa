def topological_sort(graph):
    visited = set()
    stack = []
    order = []

    for node in graph:
        if node not in visited:
            temp_stack = [node]

            while temp_stack:
                curr = temp_stack[-1]

                if curr not in visited:
                    visited.add(curr)
                    for neighbor in reversed(graph.get(curr, [])):
                        if neighbor not in visited:
                            temp_stack.append(neighbor)
                else:
                    temp_stack.pop()
                    if curr not in order:
                        order.append(curr)

    return order[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'P': ['Q', 'R'], # Disconnected part of the graph
    'Q': ['S'],
    'R': ['T']
}
print("Topological Ordering:", topological_sort(graph))