from collections import defaultdict

def find_parents(graph, root):
    parent = {root: None}
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                dfs(neighbor)

    dfs(root)
    return parent


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

parents = find_parents(graph, 'A')
for node in sorted(parents):
    print(f"Parent of {node}: {parents[node]}")