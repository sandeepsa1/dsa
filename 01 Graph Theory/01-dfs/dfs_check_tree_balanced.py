from collections import defaultdict

def is_balanced_tree(graph, root):
    balanced = True

    def dfs(node, parent):
        nonlocal balanced
        depths = []
        for neighbor in graph[node]:
            if neighbor != parent:
                d = dfs(neighbor, node)
                depths.append(d)

        if depths:
            if max(depths) - min(depths) > 1:
                balanced = False
            return 1 + max(depths)
        else:
            return 1  # Leaf node

    dfs(root, None)
    return balanced


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

print("Is the tree balanced?", is_balanced_tree(graph, 'A')) # True