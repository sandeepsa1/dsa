from collections import deque

def multi_source_bfs(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    # Step 1: Push all sources (1’s) into the queue
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
    
    # Step 2: BFS expansion
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 4 directions
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    
    return dist


matrix = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]

distances = multi_source_bfs(matrix)
for row in distances:
    print(row)          # [2, 1, 0]
                        # [1, 2, 1]
                        # [0, 1, 2]