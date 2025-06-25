# Given a 2D grid representing pixel values (e.g., grayscale 0–255), and a seed point, expand the region by
# including neighboring pixels with values close enough (within a threshold).
def region_grow(image, sr, sc, threshold):
    rows, cols = len(image), len(image[0])
    start_value = image[sr][sc]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = [[0 for _ in range(cols)] for _ in range(rows)]  # Marked region

    def is_similar(value):
        return abs(value - start_value) <= threshold

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c]:
            return
        if not is_similar(image[r][c]):
            return

        visited[r][c] = True
        result[r][c] = 1  # Mark as part of region

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return result


image = [
    [240, 239, 238, 100],
    [241, 240, 110,  90],
    [250, 251,  80,  85]
]

region = region_grow(image, 0, 0, threshold=10)

for row in region:
    print(row)      # [1, 1, 1, 0]
                    # [1, 1, 0, 0]
                    # [0, 0, 0, 0]