def find_lca_bst(tree, root, p, q):
    current = root
    while current != -1:
        if p < current and q < current:
            current = tree[current][0]
        elif p > current and q > current:
            current = tree[current][1]
        else:
            return current
    return -1


# Tree structure:
#       6
#      / \
#     2   8
#    / \ / \
#   0  4 7  9
#     / \
#    3   5
tree = {
    6: [2, 8],
    2: [0, 4],
    8: [7, 9],
    0: [-1, -1],
    4: [3, 5],
    7: [-1, -1],
    9: [-1, -1],
    3: [-1, -1],
    5: [-1, -1]
}

root = 6

lca_node = find_lca_bst(tree, root, 2, 8)
print(f"LCA of nodes 2 and 8: {lca_node}")  # 6

lca_node = find_lca_bst(tree, root, 0, 3)
print(f"LCA of nodes 0 and 3: {lca_node}")  # Output: 2
