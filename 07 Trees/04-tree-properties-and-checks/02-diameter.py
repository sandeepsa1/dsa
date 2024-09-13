def find_diameter(tree, root):
    global max_diameter
    max_diameter = 0
    
    def diameter_helper(node):
        global max_diameter        
        if node == -1 or node not in tree:
            return -1
        
        subtree_heights = []        
        for child in tree[node]:
            if child != -1:
                subtree_heights.append(diameter_helper(child) + 1)
        
        if not subtree_heights:
            return 0
        
        subtree_heights.sort(reverse=True)
        
        largest = subtree_heights[0]
        second_largest = subtree_heights[1] if len(subtree_heights) > 1 else 0
        
        max_diameter = max(max_diameter, largest + second_largest)
        
        return largest
    
    diameter_helper(root)
    return max_diameter


# Tree structure:
#         1
#        / \
#       2   3
#     / | \
#    4  5  6
#   /       \
#  8         7
tree = { 
    1: [2, 3],
    2: [4, 5, 6],
    3: [-1, -1],
    4: [8, -1],
    5: [-1, -1],
    6: [7, -1],
    7: [-1, -1],
    8: [-1, -1]
}

root = 1
diameter = find_diameter(tree, root)
print("The diameter of the non-binary tree is:", diameter) # 4 (8 -> 4 -> 2 -> 6 -> 7)