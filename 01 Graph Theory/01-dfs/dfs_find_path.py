from collections import defaultdict

def find_path(graph, start, end, path=None):
    if path is None:
        path = []

    path.append(start)

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            result = find_path(graph, neighbor, end, path[:])
            if result:
                return result

    return None


edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('D', 'H'),
    ('F', 'I'),
    ('G', 'J'),
    ('J', 'K')
]

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

path = find_path(graph, 'H', 'K')
print("Path from H to K:", path) # ['H', 'D', 'B', 'A', 'C', 'G', 'J', 'K']