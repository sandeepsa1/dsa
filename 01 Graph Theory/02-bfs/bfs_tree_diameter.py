from collections import defaultdict

def dfs_farthest(node, graph, visited, depth):
    visited.add(node)
    farthest = (node, depth)
    for neighbor in graph[node]:
        if neighbor not in visited:
            candidate = dfs_farthest(neighbor, graph, visited, depth + 1)
            if candidate[1] > farthest[1]:
                farthest = candidate
    return farthest

def tree_diameter(graph):
    visited = set()
    far_node, _ = dfs_farthest('A', graph, visited, 0)

    visited = set()
    _, diameter = dfs_farthest(far_node, graph, visited, 0)

    return diameter


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

diameter = tree_diameter(graph)
print("Maximum diameter of the tree:", diameter) # 7 H-D-B-A-C-G-J-K