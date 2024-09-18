def sorted_array_to_bst(nums):
    def build_bst(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        root = mid
        
        tree[root] = [build_bst(left, mid - 1), build_bst(mid + 1, right)]
        
        return root
    
    if not nums:
        return -1
    
    tree = {}
    
    root = build_bst(0, len(nums) - 1)
    
    return root, tree


nums = [1, 2, 3, 4, 5, 6, 7]

root, bst_tree = sorted_array_to_bst(nums)

print("Root of the BST:", root)
print("BST structure (as an adjacency list):", bst_tree)
