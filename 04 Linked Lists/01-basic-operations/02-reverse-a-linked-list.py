def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

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


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current['next']  # Store the next node
        current['next'] = prev       # Reverse the current node's pointer
        prev = current               # Move prev and current one step forward
        current = next_node

    return prev


arr = [1, 2, 3, 4, 5]
head = create_linked_list_from_array(arr)
print("Original Linked List:")
traverse(head)

head = reverse_linked_list(head)

print("Reversed Linked List:")
traverse(head)