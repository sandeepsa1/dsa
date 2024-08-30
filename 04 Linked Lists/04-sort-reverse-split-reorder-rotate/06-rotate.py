def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def rotate_right(head, k):
    if not head or not head['next'] or k == 0:
        return head

    length = 1
    current = head
    while current['next']:
        current = current['next']
        length += 1

    k = k % length
    if k == 0:
        return head

    current['next'] = head  # Connect the end of the list to the head to make it circular
    steps_to_new_head = length - k
    new_tail = head

    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail['next']

    new_head = new_tail['next']
    new_tail['next'] = None

    return new_head


# 1 -> 2 -> 3 -> 4 -> 5
head = create_node(1)
current = head
for i in range(2, 6):
    current['next'] = create_node(i)
    current = current['next']

# Rotate the linked list to the right by 2 places
k = 2
new_head = rotate_right(head, k)
traverse(new_head)