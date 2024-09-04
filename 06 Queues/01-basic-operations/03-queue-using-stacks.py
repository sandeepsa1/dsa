def initialize_queue():
    return {
        "stack1": [],
        "stack2": []
    }

def enqueue(queue_dict, element):
    queue_dict["stack1"].append(element)
    print(f"Enqueued: {element}")

def dequeue(queue_dict):
    if not queue_dict["stack2"]:
        if not queue_dict["stack1"]:
            print("Queue is empty")
            return None
        while queue_dict["stack1"]:
            queue_dict["stack2"].append(queue_dict["stack1"].pop())
    
    return queue_dict["stack2"].pop()

def is_empty(queue_dict):
    return not queue_dict["stack1"] and not queue_dict["stack2"]

def front_element(queue_dict):
    if not queue_dict["stack2"]:
        if not queue_dict["stack1"]:
            print("Queue is empty")
            return None
        while queue_dict["stack1"]:
            queue_dict["stack2"].append(queue_dict["stack1"].pop())
    
    return queue_dict["stack2"][-1]

def display(queue_dict):
    if not queue_dict["stack2"]:
        if not queue_dict["stack1"]:
            print("Queue is empty")
            return
        while queue_dict["stack1"]:
            queue_dict["stack2"].append(queue_dict["stack1"].pop())
    
    print("Queue elements:", end=" ")
    for element in reversed(queue_dict["stack2"]):
        print(element, end=" ")
    print()


queue_dict = initialize_queue()

enqueue(queue_dict, 10)
enqueue(queue_dict, 20)
enqueue(queue_dict, 30)

display(queue_dict)  # 10 20 30

print(f"Dequeued: {dequeue(queue_dict)}")  # Dequeued: 10
print(f"Dequeued: {dequeue(queue_dict)}")  # Dequeued: 20

display(queue_dict)  # 30

enqueue(queue_dict, 40)
enqueue(queue_dict, 50)

display(queue_dict)  # 30 40 50

print("Front element:", front_element(queue_dict))  # 30