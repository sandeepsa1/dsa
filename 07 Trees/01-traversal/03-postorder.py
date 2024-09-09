def postorder_traversal(tree, root):
    result = []

    def traverse(node):
        if node != -1:
            traverse(tree[node][0])
            traverse(tree[node][1])
            result.append(node)

    traverse(root)
    return result


tree = {
    4: (2, 5),
    2: (1, 3),
    5: (-1, -1),
    1: (-1, -1),
    3: (-1, -1)
}

root = 4
output = postorder_traversal(tree, root)
print("Preorder Traversal:", output)