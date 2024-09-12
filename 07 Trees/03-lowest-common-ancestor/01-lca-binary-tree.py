def find_lca(tree, root, node1, node2):
    if root == -1 or root == node1 or root == node2:
        return root
    
    left_lca = find_lca(tree, tree[root][0], node1, node2)
    right_lca = find_lca(tree, tree[root][1], node1, node2)
    
    if left_lca != -1 and right_lca != -1:
        return root
    
    return left_lca if left_lca != -1 else right_lca


tree = {
    4: (2, 5),
    2: (1, 3),
    5: (-1, -1),
    1: (-1, -1),
    3: (-1, -1)
}

root = 4

lca_node = find_lca(tree, root, 1, 2)
print(f"LCA of nodes 1 and 2: {lca_node}")  # 2

lca_node = find_lca(tree, root, 1, 5)
print(f"LCA of nodes 1 and 5: {lca_node}")  # 4