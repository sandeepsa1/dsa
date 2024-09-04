def initialize_queue(capacity):
    return {
        "queue": [None] * capacity,
        "front": -1,
        "rear": -1,
        "capacity": capacity
    }

def is_empty(queue_dict):
    return queue_dict["front"] == -1

def is_full(queue_dict):
    return (queue_dict["rear"] + 1) % queue_dict["capacity"] == queue_dict["front"]

def enqueue(queue_dict, element):
    if is_full(queue_dict):
        print("Queue is full")
        return
    
    if queue_dict["front"] == -1:
        queue_dict["front"] = 0
    
    queue_dict["rear"] = (queue_dict["rear"] + 1) % queue_dict["capacity"]
    queue_dict["queue"][queue_dict["rear"]] = element
    print(f"Enqueued: {element}")

def dequeue(queue_dict):
    if is_empty(queue_dict):
        print("Queue is empty")
        return None
    
    element = queue_dict["queue"][queue_dict["front"]]
    
    if queue_dict["front"] == queue_dict["rear"]:  # If the queue has only one element
        queue_dict["front"] = queue_dict["rear"] = -1
    else:
        queue_dict["front"] = (queue_dict["front"] + 1) % queue_dict["capacity"]
    
    print(f"Dequeued: {element}")
    return element

def front_element(queue_dict):
    if is_empty(queue_dict):
        print("Queue is empty")
        return None
    return queue_dict["queue"][queue_dict["front"]]

def display(queue_dict):
    if is_empty(queue_dict):
        print("Queue is empty")
        return
    
    print("Queue elements:", end=" ")
    i = queue_dict["front"]
    while True:
        print(queue_dict["queue"][i], end=" ")
        if i == queue_dict["rear"]:
            break
        i = (i + 1) % queue_dict["capacity"]
    print()


queue_dict = initialize_queue(5)

enqueue(queue_dict, 10)
enqueue(queue_dict, 20)
enqueue(queue_dict, 30)
enqueue(queue_dict, 40)
enqueue(queue_dict, 50)

display(queue_dict)  # 10 20 30 40 50

dequeue(queue_dict)  # Dequeued: 10
dequeue(queue_dict)  # Dequeued: 20

display(queue_dict)  # 30 40 50

enqueue(queue_dict, 60)
enqueue(queue_dict, 70)

display(queue_dict)  # 30 40 50 60 70

print("Front element:", front_element(queue_dict))  # 30

print("Is the queue full?", is_full(queue_dict))  # True