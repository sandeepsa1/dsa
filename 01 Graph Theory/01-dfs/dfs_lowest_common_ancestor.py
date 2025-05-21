from collections import defaultdict

def find_path(graph, current, target, path=None):
    if path is None:
        path = []
    path.append(current)
    if current == target:
        return path
    for neighbor in graph[current]:
        if neighbor not in path:
            res = find_path(graph, neighbor, target, path[:])
            if res:
                return res
    return None

def lowest_common_ancestor(graph, root, node1, node2):
    path1 = find_path(graph, root, node1)
    path2 = find_path(graph, root, node2)

    if not path1 or not path2:
        return None  # One of the nodes is not reachable

    lca = None
    for u, v in zip(path1, path2):
        if u == v:
            lca = u
        else:
            break
    return lca


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


print("LCA of H and K:", lowest_common_ancestor(graph, 'A', 'H', 'K'))  # A
print("LCA of D and E:", lowest_common_ancestor(graph, 'A', 'D', 'E'))  # B
print("LCA of I and K:", lowest_common_ancestor(graph, 'A', 'I', 'K'))  # C