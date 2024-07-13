from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()

        # Unlike BFS which checks, if node is visited immedietly after pop();
        # for shortest path, check for end should happen before visited check
        if node == end:
            return path + [node]

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [node]))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': ['J'],
    'J': ['K']
}

'''graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}'''

start_node = 'A'
end_node = 'K'
shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Shortest path from", start_node, "to", end_node, ":", shortest_path)
else:
    print("No path found between", start_node, "and", end_node)
