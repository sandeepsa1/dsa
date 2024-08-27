def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node['next'] = head
    return new_node  # The new node becomes the new head

def insert_at_end(head, data):
    new_node = create_node(data)
    if not head:  # If the list is empty
        return new_node
    
    current = head
    while current['next']:
        current = current['next']
    current['next'] = new_node
    return head  # The head doesn't change

def insert_after_node(prev_node, data):
    if not prev_node:
        print("Previous node must be in the linked list.")
        return
    new_node = create_node(data)
    new_node['next'] = prev_node['next']
    prev_node['next'] = new_node

def update_node(head, position, data):
    current = head
    index = 0
    while current:
        if index == position:
            current['data'] = data
            return
        current = current['next']
        index += 1
    print("Position out of range.")

def delete_node(head, key):
    current = head

    # If the node to be deleted is the head node
    if current and current['data'] == key:
        return current['next']  # Change head

    # Search for the node to be deleted, keep track of the previous node
    prev = None
    while current and current['data'] != key:
        prev = current
        current = current['next']

    # If the key was not present in the linked list
    if not current:
        print("The value is not present in the list.")
        return head

    # Unlink the node from the linked list
    prev['next'] = current['next']
    return head


# Initial linked list is empty (head is None)
head = None

# Insert elements
head = insert_at_end(head, 1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 3)
head = insert_at_beginning(head, 0)
insert_after_node(head['next'], 1.5)

# Traverse and print the linked list
print("Linked List after insertion:")
traverse(head)

# Update a node
update_node(head, 2, 10)
print("Linked List after updating the 2nd node:")
traverse(head)

# Delete a node
head = delete_node(head, 10)
print("Linked List after deleting the node with value 10:")
traverse(head)
