from collections import deque

def find_level(graph, root):
    visited = set()
    queue = deque([(root, 0)])
    max_level = 0

    while queue:
        node, level = queue.popleft()
        max_level = max(max_level, level)

        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

    return max_level


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

level = find_level(graph, 'B')
# Start A - 0: 'A'      1: 'B', 'C'     2: 'D', 'E', 'F', 'G'       3: 'H', 'I', 'J'        4: 'K'
# Start B - 0: 'B'      1: 'D', 'E'     2: 'H'
print("Level (depth) of the tree from root:", level) # A - 4, B - 2