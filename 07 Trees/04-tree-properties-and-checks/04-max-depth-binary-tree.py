def max_depth(tree, root):
    if not tree.get(root):
        return 0
    
    left_depth = max_depth(tree, tree[root][0])
    right_depth = max_depth(tree, tree[root][1])
    
    return max(left_depth, right_depth) + 1

    # For non-binary trees, instead of above 3 lines, add below.
    # depths = [max_depth(tree, child) for child in tree[root]]
    # return max(depths) + 1


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [-1, -1],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1
depth = max_depth(tree, root)
print(f"Maximum depth of the tree: {depth}")  # 3