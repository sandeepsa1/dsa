# Given a grid where:
#     0 → empty cell
#     1 → fresh orange
#     2 → rotten orange

from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # 1: Initially rotten oranges to queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, minute)
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    # 2: BFS to spread rot
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    minutes = 0

    while queue:
        r, c, minute = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, minute + 1))
                minutes = minute + 1

    # 3: If any fresh orange remains, impossible
    return minutes if fresh == 0 else -1


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print("Minutes until all oranges rot:", oranges_rotting(grid)) # 4