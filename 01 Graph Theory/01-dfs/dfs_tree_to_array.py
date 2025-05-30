from collections import defaultdict

def tree_to_array_dfs(graph, root):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(root)
    return result


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

array = tree_to_array_dfs(graph, 'A')
print("Tree as array:", array)