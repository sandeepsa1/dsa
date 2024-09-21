def serialize(tree, node):
    if node == -1:
        return ""
    
    left, right = tree.get(node, [-1, -1])
    return f"{node}({serialize(tree, left)})({serialize(tree, right)})"

def deserialize(data):
    if not data:
        return {}

    index = 0
    def helper():
        nonlocal index
        if index >= len(data) or data[index] == ')':
            index += 1  # Skip over the closing parenthesis
            return -1
        
        # Read the node value
        num = 0
        sign = 1
        if data[index] == '-':
            sign = -1
            index += 1
        
        while index < len(data) and data[index].isdigit():
            num = num * 10 + int(data[index])
            index += 1
            
        node = sign * num
        tree[node] = [-1, -1]  # Initialize children
        
        index += 1  # Skip the '('
        left_child = helper()   # Left child
        index += 1  # Skip the '('
        right_child = helper()  # Right child
        index += 1  # Skip the ')'
        
        tree[node][0] = left_child
        tree[node][1] = right_child
        
        return node

    tree = {}
    helper()
    return tree


tree = {
    1: [2, 3],
    2: [-1, -1],
    3: [-1, -1]
}

serialized_tree = serialize(tree, 1)
print("Serialized Tree:", serialized_tree)

deserialized_tree = deserialize(serialized_tree)
print("Deserialized Tree:", deserialized_tree)