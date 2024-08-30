def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def split_list_to_parts(head, k):
    length = 0
    current = head
    while current:
        length += 1
        current = current['next']
    
    part_size = length // k
    extra_nodes = length % k
    
    parts = []
    current = head
    for i in range(k):
        part_head = current
        part_length = part_size + (1 if i < extra_nodes else 0)
        
        for j in range(part_length - 1):
            if current:
                current = current['next']
        
        if current:
            next_part_head = current['next']
            current['next'] = None
            current = next_part_head
        
        parts.append(part_head)
    
    while len(parts) < k:
        parts.append(None)
    
    return parts

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
head = create_node(1)
current = head
for i in range(2, 11):
    current['next'] = create_node(i)
    current = current['next']

# Split the linked list into k = 3 parts
k = 3
parts = split_list_to_parts(head, k)

for i, part in enumerate(parts):
    print(f"Part {i + 1}:")
    traverse(part)