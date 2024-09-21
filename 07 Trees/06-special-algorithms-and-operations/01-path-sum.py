def get_node_value(node):
    if isinstance(node, int):
        return node
    return node_values[node]

def has_path_sum(node, target_sum):
    if node == -1:
        return False
    
    node_value = get_node_value(node)
    
    if tree[node][0] == -1 and tree[node][1] == -1:
        return target_sum == node_value
    
    left_child, right_child = tree[node]
    remaining_sum = target_sum - node_value
    
    return has_path_sum(left_child, remaining_sum) or has_path_sum(right_child, remaining_sum)


#           5
#          / \
#         4a  8
#        /   / \
#       11  13  4b
#      /  \      \
#     7    2      1
tree = {
    5: ['4a', 8],
    '4a': [11, -1],
    8: [13, '4b'],
    11: [7, 2],
    13: [-1, -1],
    '4b': [-1, 1],
    7: [-1, -1],
    2: [-1, -1],
    1: [-1, -1]
}

node_values = {
    '4a': 4,
    '4b': 4,
}

target_sum = 22
root = 5
result = has_path_sum(root, target_sum)
print("Path with the given sum exists:", result) # True