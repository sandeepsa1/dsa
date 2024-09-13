def is_balanced(tree, root):
    def check_balance(node):
        if node == -1:
            return 0
        
        left_height = check_balance(tree[node][0])
        if left_height == -1:
            return -1
        
        right_height = check_balance(tree[node][1])
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return check_balance(root) != -1


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [-1, -1],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1
balanced = is_balanced(tree, root)
print(f"Is the tree balanced? {balanced}")  # True