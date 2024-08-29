def create_node(data):
    return {'data': data, 'next': None}

def find_kth_to_last(head, k):
    if not head:
        return None
    
    first = head
    second = head
    
    for _ in range(k):
        if not second:
            return None
        second = second['next']
    
    while second:
        first = first['next']
        second = second['next']
    
    return first


head = create_node(1)
node2 = create_node(2)
node3 = create_node(3)
node4 = create_node(4)
node5 = create_node(5)

head['next'] = node2
node2['next'] = node3
node3['next'] = node4
node4['next'] = node5

k = 2
kth_to_last_node = find_kth_to_last(head, k)

if kth_to_last_node:
    print(f"The {k}-th to last element is:", kth_to_last_node['data'])
else:
    print(f"The linked list is shorter than {k} elements.")