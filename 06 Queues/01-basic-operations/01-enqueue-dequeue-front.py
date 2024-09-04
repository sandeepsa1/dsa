def enqueue(queue, element):
    queue.append(element)

def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        return "Queue is empty"

def front(queue):
    if not is_empty(queue):
        return queue[0]
    else:
        return "Queue is empty"

def is_empty(queue):
    return len(queue) == 0


queue = []
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print("Front element:", front(queue))  # 10

print("Dequeued element:", dequeue(queue))  # 10
print("Dequeued element:", dequeue(queue))  # 20

print("Is the queue empty?", is_empty(queue))  # False

print("Front element:", front(queue))  # 30

print("Dequeued element:", dequeue(queue))  # 30
print("Is the queue empty?", is_empty(queue))  # True
