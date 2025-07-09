def region_grow_8dir(image, sr, sc, threshold):
    rows, cols = len(image), len(image[0])
    start_value = image[sr][sc]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    def is_similar(value):
        return abs(value - start_value) <= threshold

    # 8 possible directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or not is_similar(image[r][c]):
            return

        visited[r][c] = True
        result[r][c] = 1

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return result


image = [
    [50, 51, 52, 200],
    [49, 50, 201, 199], 
    [48, 50, 202, 198]
]

region = region_grow_8dir(image, 1, 1, threshold=3)

for row in region:
    print(row)      # [1, 1, 1, 0]
                    # [1, 1, 0, 0]
                    # [1, 1, 0, 0]