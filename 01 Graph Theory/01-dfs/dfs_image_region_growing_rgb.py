# Given a 2D grid representing pixel values in RGB, and a seed point, expand the region by
# including neighboring pixels with values close enough (within a threshold).
import math

def region_grow_rgb_dfs(image, sr, sc, threshold):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]  # (R, G, B)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    def color_distance(c1, c2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c]:
            return
        if color_distance(image[r][c], start_color) > threshold:
            return

        visited[r][c] = True
        result[r][c] = 1

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return result


image = [
    [(100, 0, 0), (254, 0, 0), (200, 0, 0)],
    [(255, 1, 1), (100, 0, 0), (100, 100, 100)],
    [(250, 2, 2), (255, 0, 0), (0, 0, 255)]
]

# Run region growing from pixel (0, 0) with RGB threshold = 10
region = region_grow_rgb_dfs(image, 0, 0, threshold=50)

for row in region:
    print(row)      # [1, 0, 0]
                    # [0, 1, 0]
                    # [0, 0, 0]