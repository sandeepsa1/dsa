def create_node(data):
    return {'data': data, 'next': None}

def create_linked_list_from_array(arr):
    if not arr:
        return None
    head = create_node(arr[0])
    current = head
    for value in arr[1:]:
        new_node = create_node(value)
        current['next'] = new_node
        current = new_node
    return head

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def partition_list(head, x):
    # Dummy nodes to start the before and after lists
    before_head = create_node(0)
    after_head = create_node(0)
    
    before = before_head
    after = after_head
    
    # Traverse the original list
    current = head
    while current:
        if current['data'] < x:
            before['next'] = current
            before = before['next']
        else:
            after['next'] = current
            after = after['next']
        current = current['next']
    
    # Link the before list to the after list
    after['next'] = None  # End the after list
    before['next'] = after_head['next']  # Skip dummy head of after list
    
    # The head of the partitioned list
    return before_head['next']


arr = [1, 4, 3, 2, 5, 2]
x = 3

head = create_linked_list_from_array(arr)

print("Original List:")
traverse(head)

# Partition the list
partitioned_head = partition_list(head, x)

print(f"\nPartitioned List (x = {x}):")
traverse(partitioned_head)