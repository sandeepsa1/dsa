def find_min(tree, root):
    while tree[root][0] != -1:
        root = tree[root][0]
    return root

def insert_bst(tree, root, key):
    if root == -1:
        tree[key] = [-1, -1]
        return key
    if key < root:
        tree[root][0] = insert_bst(tree, tree[root][0], key)
    else:
        tree[root][1] = insert_bst(tree, tree[root][1], key)
    return root

def delete_bst(tree, root, key):
    if root == -1:
        return root  # Key not found
    if key < root:
        tree[root][0] = delete_bst(tree, tree[root][0], key)  # Delete from left subtree
    elif key > root:
        tree[root][1] = delete_bst(tree, tree[root][1], key)  # Delete from right subtree
    else:
        # Node with only one child or no child
        if tree[root][0] == -1:  # No left child
            temp = tree[root][1]
            del tree[root]  # Remove the node
            return temp
        elif tree[root][1] == -1:  # No right child
            temp = tree[root][0]
            del tree[root]  # Remove the node
            return temp

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = find_min(tree, tree[root][1])
        root = temp  # Replace with successor
        tree[root][1] = delete_bst(tree, tree[root][1], temp)  # Delete the inorder successor

    return root


def update_bst(tree, root, old_value, new_value):
    root = delete_bst(tree, root, old_value)
    return insert_bst(tree, root, new_value)

def inorder_traversal(tree, root):
    result = []

    def traverse(node):
        if node != -1:
            traverse(tree[node][0])
            result.append(node)
            traverse(tree[node][1])

    traverse(root)
    return result


tree = {}
root = insert_bst(tree, -1, 8)
insert_bst(tree, root, 3)
insert_bst(tree, root, 10)
insert_bst(tree, root, 1)
insert_bst(tree, root, 6)
output = inorder_traversal(tree, root)
print("BST after Insert:", output)

root = update_bst(tree, root, 6, 7)
output = inorder_traversal(tree, root)
print("BST after Update:", output)

root = delete_bst(tree, root, 10)
output = inorder_traversal(tree, root)
print("BST after Delete:", output)