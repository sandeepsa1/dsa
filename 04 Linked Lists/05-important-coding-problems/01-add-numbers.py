def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def add_two_numbers(l1, l2):
    dummy_head = create_node(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1['data'] if l1 else 0
        val2 = l2['data'] if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current['next'] = create_node(total % 10)

        current = current['next']
        if l1:
            l1 = l1['next']
        if l2:
            l2 = l2['next']

    return dummy_head['next']


# 342 (2 -> 4 -> 3) and 465 (5 -> 6 -> 4)
l1 = create_node(2)
l1['next'] = create_node(4)
l1['next']['next'] = create_node(3)

l2 = create_node(5)
l2['next'] = create_node(6)
l2['next']['next'] = create_node(4)

result = add_two_numbers(l1, l2)
traverse(result)