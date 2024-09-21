from collections import defaultdict

def find_duplicate_subtrees(tree):
    subtree_map = defaultdict(int)
    duplicates = []

    def serialize(node):
        if node == -1:
            return "#"
        
        left_child, right_child = tree.get(node, (-1, -1))
        serialized = f"{node},{serialize(left_child)},{serialize(right_child)}"
        
        subtree_map[serialized] += 1
        
        if subtree_map[serialized] == 2:
            duplicates.append(node)
        
        return serialized

    root = 1
    serialize(root)
    
    return duplicates


#        1
#       / \
#      2   3
#     /   / \
#    4   2   4
#       /
#      4
tree = {
    1: [2, 3],
    2: [4, -1],
    3: [2, 4],
    4: [-1, -1]
}

# Example use:
duplicates = find_duplicate_subtrees(tree)
print("Duplicate subtree roots are:", duplicates) # [4, 2]