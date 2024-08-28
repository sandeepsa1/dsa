import heapq

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

def merge_k_sorted_lists(lists):
    heap = []
    
    # Initialize the heap with the head of each list
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i]['data'], i, lists[i]))
    
    # Dummy node to help with merging
    dummy = create_node(0)
    current = dummy
    
    while heap:
        # Get the smallest element from the heap
        value, i, node = heapq.heappop(heap)
        
        # Add the smallest node to the merged list
        current['next'] = node
        current = current['next']
        
        # If the node has a next, push it into the heap
        if node['next']:
            heapq.heappush(heap, (node['next']['data'], i, node['next']))
    
    return dummy['next']


arr1 = [1, 4, 7]
arr2 = [2, 5, 8]
arr3 = [3, 6, 9]

l1 = create_linked_list_from_array(arr1)
l2 = create_linked_list_from_array(arr2)
l3 = create_linked_list_from_array(arr3)

print("List 1:")
traverse(l1)
print("List 2:")
traverse(l2)
print("List 3:")
traverse(l3)

# Merge the k sorted lists
merged_head = merge_k_sorted_lists([l1, l2, l3])

print("\nMerged List:")
traverse(merged_head)