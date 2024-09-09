from collections import deque

def level_order_traversal(tree, root):
    if root == -1:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node)

        # Add the left child to the queue if it exists
        if tree[node][0] != -1:
            queue.append(tree[node][0])

        # Add the right child to the queue if it exists
        if tree[node][1] != -1:
            queue.append(tree[node][1])

    return result


tree = {
    4: (2, 5),
    2: (1, 3),
    5: (-1, -1),
    1: (-1, -1),
    3: (-1, -1)
}

root = 4
output = level_order_traversal(tree, root)
print("Preorder Traversal:", output)