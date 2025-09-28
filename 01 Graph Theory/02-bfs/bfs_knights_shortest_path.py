from collections import deque

def knight_shortest_path(N, start, target):
    # All 8 possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited.add(start)
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == target:
            return dist  # Found shortest path
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1  # No path (shouldn't happen on chessboard)


N = 8  # 8x8 chessboard
start = (0, 0)
target = (7, 7)

print("Minimum knight moves:", knight_shortest_path(N, start, target))