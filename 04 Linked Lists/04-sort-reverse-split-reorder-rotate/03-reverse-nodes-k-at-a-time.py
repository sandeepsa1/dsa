def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def reverse_k_group(head, k):
    current = head
    count = 0

    while current and count < k:
        current = current['next']
        count += 1

    if count == k:
        current = head
        prev = None
        next_node = None
        count = 0

        # Reverse k nodes
        while current and count < k:
            next_node = current['next']
            current['next'] = prev
            prev = current
            current = next_node
            count += 1

        # next_node is now the (k+1)th node
        # Recursively call for the list starting from current
        # And make the rest of the list as the next of the last node in the current k-group
        if next_node:
            head['next'] = reverse_k_group(next_node, k)

        return prev

    return head

# 1 -> 2 -> 3 -> 4 -> 5
head = create_node(1)
head['next'] = create_node(2)
head['next']['next'] = create_node(3)
head['next']['next']['next'] = create_node(4)
head['next']['next']['next']['next'] = create_node(5)

# Reverse the linked list in groups of k = 2
k = 2
new_head = reverse_k_group(head, k)
traverse(new_head)