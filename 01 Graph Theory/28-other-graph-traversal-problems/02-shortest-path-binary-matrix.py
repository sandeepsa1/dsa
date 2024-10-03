from collections import deque

def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    n = len(grid)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    queue = deque([(0, 0, 1)])
    
    grid[0][0] = 1

    while queue:
        row, col, path_length = queue.popleft()

        if row == n - 1 and col == n - 1:
            return path_length

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                queue.append((new_row, new_col, path_length + 1))
                grid[new_row][new_col] = 1

    return -1


grid = [
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]

print(shortestPathBinaryMatrix(grid))  # 3