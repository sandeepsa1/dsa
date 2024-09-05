from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0
    time = 0

    # Step 1: Add all rotten oranges to the queue and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # Step 2: BFS to rot the fresh oranges
    while queue:
        r, c, current_time = queue.popleft()
        time = max(time, current_time)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc, current_time + 1))

    # Step 3: If there are still fresh oranges, return -1, else return the time
    return -1 if fresh_oranges > 0 else time


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid))  # 4