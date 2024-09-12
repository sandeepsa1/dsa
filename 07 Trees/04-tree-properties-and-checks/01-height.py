def compute_height(tree, root):
    if root == -1:
        return -1
    
    left_height = compute_height(tree, tree[root][0])
    right_height = compute_height(tree, tree[root][1])
    
    return max(left_height, right_height) + 1


# Tree structure:
#       1
#      / \
#     2   3
#    / \
#   4   5
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [-1, -1],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1
height = compute_height(tree, root)
print(f"Height of the tree: {height}")  # 2