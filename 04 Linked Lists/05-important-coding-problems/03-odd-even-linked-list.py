def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def odd_even_list(head):
    if not head or not head['next']:
        return head

    odd = head
    even = head['next']
    even_head = even

    while even and even['next']:
        odd['next'] = even['next']
        odd = odd['next']
        even['next'] = odd['next']
        even = even['next']

    odd['next'] = even_head

    return head


# 1 -> 2 -> 3 -> 4 -> 5
head = create_node(1)
head['next'] = create_node(2)
head['next']['next'] = create_node(3)
head['next']['next']['next'] = create_node(4)
head['next']['next']['next']['next'] = create_node(5)

new_head = odd_even_list(head)
traverse(new_head)