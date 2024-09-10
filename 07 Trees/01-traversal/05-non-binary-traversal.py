from collections import deque

def preorder_traversal_nary(tree, root):
    result = []

    def traverse(node):
        if node != -1:
            result.append(node)
            for child in tree.get(node, []):
                traverse(child)

    traverse(root)
    return result

def postorder_traversal_nary(tree, root):
    result = []

    def traverse(node):
        if node != -1:
            for child in tree.get(node, []):
                traverse(child)
            result.append(node)

    traverse(root)
    return result

def level_order_traversal_nary(tree, root):
    if root == -1:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node)

        for child in tree.get(node, []):
            queue.append(child)

    return result


tree = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

root = 1
output = preorder_traversal_nary(tree, root)
print("Preorder Traversal:", output)

output = postorder_traversal_nary(tree, root)
print("Postorder Traversal:", output)

output = level_order_traversal_nary(tree, root)
print("Level Order Traversal:", output)