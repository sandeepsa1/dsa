def insert_bst(tree, root, key):
    if root == -1:
        tree[key] = [-1, -1]
        return key
    if key < root:
        tree[root][0] = insert_bst(tree, tree[root][0], key)
    else:
        tree[root][1] = insert_bst(tree, tree[root][1], key)
    return root

def min_abs_diff_bst(tree, root):
    stack = []
    current = root
    prev = None
    min_diff = float('inf')
    
    while current != -1 or stack:
        while current != -1:
            stack.append(current)
            current = tree[current][0]
        
        current = stack.pop()
        
        if prev is not None:
            min_diff = min(min_diff, current - prev)
        
        prev = current
        
        current = tree[current][1]
    
    return min_diff

tree = {}
root = insert_bst(tree, -1, 8)
insert_bst(tree, root, 3)
insert_bst(tree, root, 10)
insert_bst(tree, root, 1)
insert_bst(tree, root, 6)
insert_bst(tree, root, 14)

print(min_abs_diff_bst(tree, root))  # 2