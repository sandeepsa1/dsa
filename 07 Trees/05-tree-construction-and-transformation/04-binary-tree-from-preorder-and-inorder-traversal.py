def build_tree(preorder, inorder):
    def build_subtree(preorder_left, preorder_right, inorder_left, inorder_right):
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return -1
        
        root_value = preorder[preorder_left]
        root_index_in_inorder = inorder_map[root_value]
        
        left_subtree_size = root_index_in_inorder - inorder_left
        
        left_child = build_subtree(preorder_left + 1, preorder_left + left_subtree_size, inorder_left, root_index_in_inorder - 1)
        
        right_child = build_subtree(preorder_left + left_subtree_size + 1, preorder_right, root_index_in_inorder + 1, inorder_right)
        
        tree[root_value] = [left_child, right_child]
        return root_value
    
    if not preorder or not inorder:
        return -1
    
    inorder_map = {value: idx for idx, value in enumerate(inorder)}
    
    tree = {}
    
    root = build_subtree(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    return root, tree


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root, constructed_tree = build_tree(preorder, inorder)
print("Root of the constructed tree:", root)
print("Constructed tree (as an adjacency list):", constructed_tree)