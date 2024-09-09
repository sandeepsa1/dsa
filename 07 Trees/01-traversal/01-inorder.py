def inorder_traversal(tree, root):
    result = []

    def traverse(node):
        if node != -1:
            traverse(tree[node][0])   # Visit left subtree
            result.append(node)       # Visit root
            traverse(tree[node][1])   # Visit right subtree

    traverse(root)
    return result

# Example tree represented as an adjacency list
# Tree structure:
#       4
#      / \
#     2   5
#    / \
#   1   3
tree = {
    4: (2, 5),  # Node 4 has left child 2 and right child 5
    2: (1, 3),  # Node 2 has left child 1 and right child 3
    5: (-1, -1),# Node 5 is a leaf node
    1: (-1, -1),# Node 1 is a leaf node
    3: (-1, -1) # Node 3 is a leaf node
}

root = 4
output = inorder_traversal(tree, root)
print("Inorder Traversal:", output)