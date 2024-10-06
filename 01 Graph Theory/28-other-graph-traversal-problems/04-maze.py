from collections import deque

def shortestPathInMaze(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    
    if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
        return -1
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = set([(start[0], start[1])])
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == destination:
            return dist
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))
    
    return -1


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
destination = (4, 4)

result = shortestPathInMaze(maze, start, destination)
print(f"Shortest path length: {result}")