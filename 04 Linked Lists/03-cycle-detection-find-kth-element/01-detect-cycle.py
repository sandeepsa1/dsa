def create_node(data):
    return {'data': data, 'next': None}

def detect_cycle(head):
    if not head or not head['next']:
        return None
    
    slow = head
    fast = head
    
    while fast and fast['next']:
        slow = slow['next']
        fast = fast['next']['next']
        
        if slow == fast:
            return slow
    
    return None

def find_cycle_start(head, meeting_point):
    start = head
    
    while start != meeting_point:
        start = start['next']
        meeting_point = meeting_point['next']
    
    return start

def get_cycle_nodes(cycle_start):
    cycle_nodes = []
    current = cycle_start
    
    while True:
        cycle_nodes.append(current['data'])
        current = current['next']
        if current == cycle_start:
            break
    
    return cycle_nodes


# 1 -> 2 -> 3 -> 4 -> 5 -> 3
head = create_node(1)
node2 = create_node(2)
node3 = create_node(3)
node4 = create_node(4)
node5 = create_node(5)

head['next'] = node2
node2['next'] = node3
node3['next'] = node4
node4['next'] = node5
node5['next'] = node3

meeting_point = detect_cycle(head)

if meeting_point:
    cycle_start = find_cycle_start(head, meeting_point)
    cycle_nodes = get_cycle_nodes(cycle_start)
    print("Cycle detected at node with value:", cycle_start['data'])
    print("Nodes in the cycle:", cycle_nodes)
else:
    print("No cycle detected in the linked list.")