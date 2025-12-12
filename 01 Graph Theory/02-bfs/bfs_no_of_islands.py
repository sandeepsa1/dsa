from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)

    return islands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid)) # 3