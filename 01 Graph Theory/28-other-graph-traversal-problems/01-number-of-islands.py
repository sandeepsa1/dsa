from collections import deque

def numIslandsBFS(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'
        while queue:
            row, col = queue.popleft()
            for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    queue.append((x, y))
                    grid[x][y] = '0'

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                num_islands += 1
                bfs(r, c)

    return num_islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslandsBFS(grid))  # 3