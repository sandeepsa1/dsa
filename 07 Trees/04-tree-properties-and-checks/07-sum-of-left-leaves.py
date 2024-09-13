def sum_of_left_leaves(tree, root):
    def is_leaf(node):
        return node != -1 and tree[node][0] == -1 and tree[node][1] == -1

    def sum_left_leaves(node):
        if node == -1:
            return 0
        
        total_sum = 0
        
        left = tree[node][0]
        if is_leaf(left):
            total_sum += left
        
        total_sum += sum_left_leaves(left)
        total_sum += sum_left_leaves(tree[node][1])

        ''' For right leaves
        right = tree[node][1]
        if is_leaf(right):
            total_sum += right
        
        total_sum += sum_left_leaves(tree[node][0])
        total_sum += sum_left_leaves(right) '''
        
        return total_sum

    return sum_left_leaves(root)


# Tree structure:
#       1
#      / \
#     2   3
#    /     \
#   4       5
tree = {
    1: [2, 3],
    2: [4, -1],
    3: [-1, 5],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1
result = sum_of_left_leaves(tree, root)
print(f"Sum of all left leaves: {result}")  # 4