from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    queue.append("1")
    
    result = []
    
    for _ in range(n):
        current = queue.popleft()
        result.append(current)
        
        queue.append(current + "0")
        queue.append(current + "1")
    
    return result

n = 10
binary_numbers = generate_binary_numbers(n)
for number in binary_numbers:
    print(number)