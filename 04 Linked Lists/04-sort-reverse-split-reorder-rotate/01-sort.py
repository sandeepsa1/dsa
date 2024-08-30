def create_node(data):
    return {'data': data, 'next': None}

def traverse(head):
    current = head
    while current:
        print(current['data'], end=" -> ")
        current = current['next']
    print("None")

def find_middle(head):
    slow = head
    fast = head
    prev = None
    
    while fast and fast['next']:
        prev = slow
        slow = slow['next']
        fast = fast['next']['next']
    
    if prev:
        prev['next'] = None 
    
    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left['data'] <= right['data']:
        result = left
        result['next'] = merge_sorted_lists(left['next'], right)
    else:
        result = right
        result['next'] = merge_sorted_lists(left, right['next'])
    
    return result

def merge_sort_linked_list(head):
    if not head or not head['next']:
        return head
    
    middle = find_middle(head)
    
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(middle)
    
    sorted_list = merge_sorted_lists(left, right)
    
    return sorted_list


# 4 -> 2 -> 1 -> 3
head = create_node(4)
head['next'] = create_node(2)
head['next']['next'] = create_node(1)
head['next']['next']['next'] = create_node(3)

sorted_head = merge_sort_linked_list(head)
traverse(sorted_head)