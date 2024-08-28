def create_node(data):
    return {'data': data, 'next': None}

def find_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current['next']
    return length

def find_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    # Get the lengths of both linked lists
    lengthA = find_length(headA)
    lengthB = find_length(headB)
    
    # Calculate the difference in lengths
    diff = abs(lengthA - lengthB)
    
    # Align the start pointers for both linked lists
    if lengthA > lengthB:
        for _ in range(diff):
            headA = headA['next']
    else:
        for _ in range(diff):
            headB = headB['next']
    
    # Traverse both lists together to find the intersection
    while headA and headB:
        if headA == headB:
            return headA  # Intersection found
        headA = headA['next']
        headB = headB['next']
    
    return None  # No intersection

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")


# Creating the first linked list: 1 -> 3 -> 5 -> 7 -> 9
headA = create_node(1)
node2 = create_node(3)
node3 = create_node(5)
node4 = create_node(7)
node5 = create_node(9)
headA['next'] = node2
node2['next'] = node3
node3['next'] = node4
node4['next'] = node5

# Creating the second linked list: 2 -> 4 -> 7 -> 9 (intersects at node 7)
headB = create_node(2)
node7 = create_node(4)
headB['next'] = node7
node7['next'] = node4  # Intersection starts here

print("List A:")
traverse(headA)

print("List B:")
traverse(headB)

# Find intersection node
intersection_node = find_intersection_node(headA, headB)

if intersection_node:
    print("\nIntersection at node with value:", intersection_node['data'])
else:
    print("\nNo intersection found.")