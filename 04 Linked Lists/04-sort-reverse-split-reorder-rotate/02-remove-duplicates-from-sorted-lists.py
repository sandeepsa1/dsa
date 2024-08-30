def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def remove_duplicates(head):
    current = head
    
    while current and current['next']:
        if current['data'] == current['next']['data']:
            current['next'] = current['next']['next']
        else:
            current = current['next']
    
    return head


# 1 -> 1 -> 2 -> 3 -> 3
head = create_node(1)
head['next'] = create_node(1)
head['next']['next'] = create_node(2)
head['next']['next']['next'] = create_node(3)
head['next']['next']['next']['next'] = create_node(3)

head = remove_duplicates(head)
traverse(head)
