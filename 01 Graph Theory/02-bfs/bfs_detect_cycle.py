from collections import deque

def has_cycle_bfs(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque([(start, None)])  # (current_node, parent_node)

            while queue:
                node, parent = queue.popleft()
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True  # Cycle detected

    return False  # No cycle found


graph_with_cycle = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'A']  # A cycle: A-B-C-D-A
}

print("Cycle in graph_with_cycle?", has_cycle_bfs(graph_with_cycle))   # True