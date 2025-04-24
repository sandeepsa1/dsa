from collections import defaultdict

def count_leaves(graph, root):
    visited = set()
    def dfs(node):
        visited.add(node)
        children = [n for n in graph[node] if n not in visited]
        if not children:
            return 1
        return sum(dfs(child) for child in children)
    return dfs(root)


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

print("Leaf nodes:", count_leaves(graph, 'A'))