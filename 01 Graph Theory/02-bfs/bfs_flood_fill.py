from collections import deque

def flood_fill_bfs(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    if original_color == new_color:
        return image  # nothing to change

    queue = deque([(sr, sc)])
    image[sr][sc] = new_color  # fill starting pixel

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image


image = [
    [1, 1, 0, 1],
    [1, 3, 0, 2],
    [1, 2, 0, 2]
]

sr, sc = 0, 0  # starting point
new_color = 9

filled_image = flood_fill_bfs(image, sr, sc, new_color)
for row in filled_image:
    print(row)                  # [9, 9, 0, 2]
                                # [9, 0, 0, 2]
                                # [9, 9, 0, 2]