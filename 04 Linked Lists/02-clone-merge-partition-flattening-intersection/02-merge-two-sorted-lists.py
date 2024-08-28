def create_node(data):
    return {'data': data, 'next': None}

def create_linked_list_from_array(arr):
    if not arr:
        return None
    head = create_node(arr[0])
    current = head
    for value in arr[1:]:
        new_node = create_node(value)
        current['next'] = new_node
        current = new_node
    return head

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def merge_two_sorted_lists(l1, l2):
    # Dummy node to help with merging
    dummy = create_node(0)
    tail = dummy
    
    # Traverse both lists
    while l1 and l2:
        if l1['data'] < l2['data']:
            tail['next'] = l1
            l1 = l1['next']
        else:
            tail['next'] = l2
            l2 = l2['next']
        tail = tail['next']
    
    # Append the remaining nodes from l1 or l2
    if l1:
        tail['next'] = l1
    else:
        tail['next'] = l2
    
    return dummy['next']


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

l1 = create_linked_list_from_array(arr1)
l2 = create_linked_list_from_array(arr2)

print("List 1:")
traverse(l1)
print("List 2:")
traverse(l2)

# Merge the two sorted lists
merged_head = merge_two_sorted_lists(l1, l2)

print("\nMerged List:")
traverse(merged_head)