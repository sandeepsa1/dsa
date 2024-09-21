def inorder(tree, node, result):
    if node == -1:
        return
    left, right = tree.get(node, [-1, -1])
    inorder(tree, left, result)
    result.append(node)
    inorder(tree, right, result)

def recover_bst(tree):
    result = []
    inorder(tree, 3, result)
    print("Inorder traversal before fixing:", result)

    x, y = -1, -1
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            y = result[i + 1]
            if x == -1:
                x = result[i]
            else:
                break
    
    if x != -1 and y != -1:
        swap(tree, x, y)

def swap(tree, x, y):
    for node in tree:
        left, right = tree[node]
        if left == x:
            tree[node][0] = y
        elif left == y:
            tree[node][0] = x
        if right == x:
            tree[node][1] = y
        elif right == y:
            tree[node][1] = x


tree = {
    3: [1, 4],
    1: [-1, -1],
    4: [5, 2],  # Swapped nodes 2 and 5
    5: [-1, -1],
    2: [-1, -1]
}

recover_bst(tree)
print("Tree after fixing:", tree)