def compute_diameter(tree, root):
    global max_diameter
    max_diameter = 0
    
    def height(node):
        global max_diameter
        if node == -1:
            return -1
        
        left_height = height(tree[node][0])
        right_height = height(tree[node][1])
        
        max_diameter = max(max_diameter, left_height + right_height + 2)
        
        return max(left_height, right_height) + 1
    
    height(root)
    
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
diameter = compute_diameter(tree, root)
print(f"Diameter of the tree: {diameter}")  # 4 (8 -> 4 -> 2 -> 6 -> 7)