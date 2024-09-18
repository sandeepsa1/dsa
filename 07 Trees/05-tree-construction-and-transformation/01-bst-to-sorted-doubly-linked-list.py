def bst_to_doubly_linked_list(root):
    def inorder(node):
        nonlocal prev, head
        
        if node == -1:
            return
        
        inorder(tree[node][0])
        
        if prev[0] is not None:
            tree[prev[0]][1] = node
            tree[node][0] = prev[0]
        else:
            head = node
        
        prev[0] = node
        
        inorder(tree[node][1])
    
    if root == -1:
        return None
    
    prev = [None]
    head = None
    
    inorder(root)
    
    return head


tree = {
    4: [2, 6],
    2: [1, 3],
    6: [5, 7],
    1: [-1, -1],
    3: [-1, -1],
    5: [-1, -1],
    7: [-1, -1]
}

root = 4

head = bst_to_doubly_linked_list(root)

current = head
while current != -1:
    print(current, end=" <-> " if tree[current][1] != -1 else "\n")
    current = tree[current][1]