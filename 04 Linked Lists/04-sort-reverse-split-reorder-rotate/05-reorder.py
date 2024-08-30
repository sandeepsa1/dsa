def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def find_middle(head):
    slow = fast = head
    while fast and fast['next']:
        slow = slow['next']
        fast = fast['next']['next']
    return slow

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current['next']
        current['next'] = prev
        prev = current
        current = next_node
    return prev

def reorder_list(head):
    if not head or not head['next']:
        return head

    middle = find_middle(head)

    second_half = reverse_list(middle)
    
    first_half = head
    while second_half['next']:
        temp1 = first_half['next']
        temp2 = second_half['next']

        first_half['next'] = second_half
        second_half['next'] = temp1

        first_half = temp1
        second_half = temp2

    return head


# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = create_node(1)
current = head
for i in range(2, 8):
    current['next'] = create_node(i)
    current = current['next']

reorder_list(head)
traverse(head)
