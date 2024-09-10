def insert_bst(tree, root, key):
    if root == -1:
        tree[key] = [-1, -1]
        return key
    if key < root:
        tree[root][0] = insert_bst(tree, tree[root][0], key)
    else:
        tree[root][1] = insert_bst(tree, tree[root][1], key)
    return root

def search_bst(tree, root, key):
    if root == -1:
        return False
    
    if key == root:
        return True
    
    if key < root:
        return search_bst(tree, tree[root][0], key)
    
    return search_bst(tree, tree[root][1], key)


tree = {}
root = insert_bst(tree, -1, 8)
insert_bst(tree, root, 3)
insert_bst(tree, root, 10)
insert_bst(tree, root, 1)
insert_bst(tree, root, 6)
insert_bst(tree, root, 14)

print(search_bst(tree, root, 6))  # True
print(search_bst(tree, root, 5))  # False