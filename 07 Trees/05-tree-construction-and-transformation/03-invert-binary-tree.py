def invert_binary_tree(node):
    if node == -1:
        return -1
    
    left_inverted = invert_binary_tree(tree[node][0])
    right_inverted = invert_binary_tree(tree[node][1])
    
    tree[node] = [right_inverted, left_inverted]

    ''' For non-binary trees, replace above three lines with below
    for i in range(len(tree[node])):
        tree[node][i] = invert_binary_tree(tree[node][i])
    tree[node].reverse()'''
    
    return node


#       1               1
#      / \             / \
#     2   3           3   2
#    / \                 / \
#   4   5               5   4
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [-1, -1],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1

inverted_root = invert_binary_tree(root)
print("Inverted Binary Tree:", tree)