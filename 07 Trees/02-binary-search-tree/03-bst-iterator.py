def insert_bst(tree, root, key):
    if root == -1:
        tree[key] = [-1, -1]
        return key
    if key < root:
        tree[root][0] = insert_bst(tree, tree[root][0], key)
    else:
        tree[root][1] = insert_bst(tree, tree[root][1], key)
    return root

class BSTIterator:
    def __init__(self, tree, root):
        self.stack = []
        self.tree = tree
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root != -1:
            self.stack.append(root)
            root = self.tree[root][0]

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        topmost_node = self.stack.pop()

        if self.tree[topmost_node][1] != -1:
            self._leftmost_inorder(self.tree[topmost_node][1])

        return topmost_node


tree = {}
root = insert_bst(tree, -1, 8)
insert_bst(tree, root, 3)
insert_bst(tree, root, 10)
insert_bst(tree, root, 1)
insert_bst(tree, root, 6)
insert_bst(tree, root, 14)

iterator = BSTIterator(tree, root)

while iterator.hasNext():
    print(iterator.next())