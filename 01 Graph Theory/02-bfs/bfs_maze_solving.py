from collections import deque

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start, [start])])  # (position, path_so_far)

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path  # Found the end
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                maze[nr][nc] == '0' and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None  # No path found


maze = [
    ['0', '1', '0', '0', '0'],
    ['0', '1', '0', '1', '0'],
    ['0', '0', '0', '1', '0'],
    ['0', '1', '1', '0', '0'],
    ['0', '0', '0', '0', '1'],
]

start = (0, 0)
end = (4, 3)

path = bfs_maze_solver(maze, start, end)
if path:
    print("Shortest path found:", path) # [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)] - 8
    print("Length:", len(path))
else:
    print("No path found.")