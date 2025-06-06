from collections import defaultdict

def build_directed_tree(graph, root):
    tree = defaultdict(list)
    visited = set()

    def dfs(node, parent=None):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                tree[node].append(neighbor)
                dfs(neighbor, node)
    dfs(root)
    return tree

def mirror_tree(tree, node):
    tree[node].reverse()  # Reverse children
    for child in tree[node]:
        mirror_tree(tree, child)

def print_tree(tree, node, depth=0):
    print("  " * depth + node)
    for child in tree[node]:
        print_tree(tree, child, depth + 1)


edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('D', 'H'),
    ('F', 'I'),
    ('G', 'J'),
    ('J', 'K')
]

undirected = defaultdict(list)
for u, v in edges:
    undirected[u].append(v)
    undirected[v].append(u)

tree = build_directed_tree(undirected, 'A')
print("Original Tree:")
print_tree(tree, 'A')

mirror_tree(tree, 'A')

print("\nMirrored Tree:")
print_tree(tree, 'A')