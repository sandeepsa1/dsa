def create_node(data):
    return {'data': data, 'next': None, 'prev': None, 'child': None}

def flatten(head):
    if not head:
        return None
    
    stack = []
    current = head
    
    while current:
        if current['child']:
            # If there's a next node, push it onto the stack
            if current['next']:
                stack.append(current['next'])
                
            # Link the child list into the main list
            current['next'] = current['child']
            if current['next']:
                current['next']['prev'] = current
            
            # Remove the child pointer
            current['child'] = None
        
        # If we reach the end of a list and there's something on the stack
        if not current['next'] and stack:
            # Pop from the stack and continue
            current['next'] = stack.pop()
            current['next']['prev'] = current
        
        # Move to the next node
        current = current['next']
    
    return head

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" <-> ")
        current = current['next']
    print("None")


head = create_node(1)
second = create_node(2)
third = create_node(3)
fourth = create_node(4)
fifth = create_node(5)
sixth = create_node(6)
child1 = create_node(7)
child2 = create_node(8)
child3 = create_node(9)

# Main list
head['next'] = second
second['prev'] = head
second['next'] = third
third['prev'] = second
third['next'] = fourth
fourth['prev'] = third
fourth['next'] = fifth
fifth['prev'] = fourth
fifth['next'] = sixth
sixth['prev'] = fifth

# Child list for node 3
third['child'] = child1
child1['next'] = child2
child2['prev'] = child1
child2['child'] = child3

print("Original Multilevel Doubly Linked List:")
traverse(head)

# Flatten the list
flattened_head = flatten(head)

print("\nFlattened Doubly Linked List:")
traverse(flattened_head)