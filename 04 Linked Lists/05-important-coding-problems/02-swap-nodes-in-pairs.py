def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def swap_pairs(head):
    dummy = create_node(0)
    dummy['next'] = head
    prev = dummy

    while prev['next'] and prev['next']['next']:
        first = prev['next']
        second = prev['next']['next']

        first['next'] = second['next']
        second['next'] = first
        prev['next'] = second

        prev = first

    return dummy['next']


# 1 -> 2 -> 3 -> 4
head = create_node(1)
head['next'] = create_node(2)
head['next']['next'] = create_node(3)
head['next']['next']['next'] = create_node(4)

new_head = swap_pairs(head)
traverse(new_head)