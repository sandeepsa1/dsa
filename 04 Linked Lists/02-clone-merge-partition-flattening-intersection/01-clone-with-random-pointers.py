def create_node(data):
    return {'data': data, 'next': None, 'random': None}

def create_linked_list_with_random(arr, random_indices):
    if not arr:
        return None
    nodes = [create_node(value) for value in arr]
    for i in range(len(arr) - 1):
        nodes[i]['next'] = nodes[i + 1]
    for i, random_index in enumerate(random_indices):
        if random_index is not None:
            nodes[i]['random'] = nodes[random_index]
    return nodes[0]

def traverse_with_random(head):
    current = head
    while current:
        random_data = current['random']['data'] if current['random'] else None
        print(f"Node: {current['data']} | Random: {random_data}")
        current = current['next']
    print("End of list")

def clone_linked_list_with_random(head):
    if not head:
        return None
    
    # First pass: Create new nodes and insert them next to original nodes
    current = head
    while current:
        new_node = create_node(current['data'])
        new_node['next'] = current['next']
        current['next'] = new_node
        current = new_node['next']
    
    # Second pass: Set random pointers for the new nodes
    current = head
    while current:
        if current['random']:
            current['next']['random'] = current['random']['next']
        current = current['next']['next']
    
    # Third pass: Separate the original list and the cloned list
    original = head
    clone = head['next']
    clone_head = clone
    
    while original:
        original['next'] = original['next']['next']
        if clone['next']:
            clone['next'] = clone['next']['next']
        original = original['next']
        clone = clone['next']
    
    return clone_head


arr = [1, 2, 3, 4, 5]
random_indices = [None, 0, 4, 2, 1]
head = create_linked_list_with_random(arr, random_indices)

print("Original Linked List with Random Pointers:")
traverse_with_random(head)

# Clone the linked list
cloned_head = clone_linked_list_with_random(head)

print("\nCloned Linked List with Random Pointers:")
traverse_with_random(cloned_head)