def compute_diameter(tree, root):
    global max_diameter
    max_diameter = 0
    
    def height(node):
        global max_diameter
        if node == -1:
            return -1
        
        left_height = height(tree[node][0])
        right_height = height(tree[node][1])
        
        max_diameter = left_height + right_height + 2
        
        max_diameter = max(max_diameter, left_height + right_height + 2)
        
        return max(left_height, right_height) + 1
    
    height(root)
    
    return diameter


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [-1, -1],
    4: [-1, -1],
    5: [-1, -1]
}

root = 1
# The diameter is the longest path between two nodes. In this tree, the longest path is between nodes 4 and 5,
# passing through node 2 and 1. The path has 3 edges (4 → 2 → 1 → 3).
diameter = compute_diameter(tree, root)
print(f"Diameter of the tree: {diameter}")  # 3