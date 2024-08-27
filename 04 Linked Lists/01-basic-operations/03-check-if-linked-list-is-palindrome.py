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

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current['next']
        current['next'] = prev
        prev = current
        current = next_node
    return prev

def is_palindrome(head):
    if not head or not head['next']:
        return True
    
    slow = fast = head
    while fast and fast['next']:
        slow = slow['next']
        fast = fast['next']['next']
    
    second_half_head = reverse_linked_list(slow)
    
    first_half_head = head
    while second_half_head:
        if first_half_head['data'] != second_half_head['data']:
            return False
        first_half_head = first_half_head['next']
        second_half_head = second_half_head['next']
    
    return True


arr = [1, 2, 3, 2, 1]
head = create_linked_list_from_array(arr)
print("Original Linked List:")
traverse(head)

result = is_palindrome(head)
print("Is the linked list a palindrome?", result)