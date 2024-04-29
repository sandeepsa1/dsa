from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [node, neighbor]
                else:
                    queue.append((neighbor, path + [node]))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'
shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Shortest path from", start_node, "to", end_node, ":", shortest_path)
else:
    print("No path found between", start_node, "and", end_node)