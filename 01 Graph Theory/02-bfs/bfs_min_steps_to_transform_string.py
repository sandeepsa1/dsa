from collections import deque

def min_operations_string(start, target):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps
        
        # generate neighbors (edit operations)
        for i in range(len(word)):
            # delete
            neighbor = word[:i] + word[i+1:]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
            
            # replace
            for c in "abcdefghijklmnopqrstuvwxyz":
                neighbor = word[:i] + c + word[i+1:]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        # insert at any position
        for i in range(len(word) + 1):
            for c in "abcdefghijklmnopqrstuvwxyz":
                neighbor = word[:i] + c + word[i:]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
    
    return -1


print(min_operations_string("cat", "dog")) # 3 (cat → dat → dot → dog)
print(min_operations_string("ab", "cd")) # 2