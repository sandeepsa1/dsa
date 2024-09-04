from collections import deque


def level_order_traversal(binary_tree, root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()        
        print(current_node, end=" ")
        
        left_child, right_child = binary_tree.get(current_node, [])
        
        if left_child is not None:
            queue.append(left_child)
        if right_child is not None:
            queue.append(right_child)



binary_tree = {
    1: [2, 3],
    2: [4, 5],
    3: [None, 6],
    4: [None, None],
    5: [None, None],
    6: [None, None]
}

root = 1
level_order_traversal(binary_tree, root)