def is_symmetric(tree, root):
    def is_mirror(left, right):
        if left == -1 and right == -1:
            return True
        
        if left == -1 or right == -1:
            return False
        
        return is_mirror(tree[left][0], tree[right][1]) and is_mirror(tree[left][1], tree[right][0])

    if root == -1:
        return True

    return is_mirror(tree[root][0], tree[root][1])


tree = {
    1: [2, 2],
    2: [3, 4],
    3: [-1, -1],
    4: [-1, -1]
}

root = 1
symmetric = is_symmetric(tree, root)
print(f"Is the tree symmetric? {symmetric}") # True