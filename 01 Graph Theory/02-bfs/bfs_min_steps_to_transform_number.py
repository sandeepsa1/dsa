from collections import deque

def min_operations_number(start, target):
    queue = deque([(start, 0)])  # (number, steps)
    visited = set([start])

    while queue:
        num, steps = queue.popleft()
        if num == target:
            return steps

        # allowed moves
        for next_num in (num - 1, num + 1, num * 2):
            if 0 <= next_num <= 10000 and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))
    
    return -1


print(min_operations_number(4, 17)) # 4  → 8  → 16 → 17 (3 steps)