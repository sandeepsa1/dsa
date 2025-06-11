# Flood fill is used to "fill" a connected region (like paint bucket in MS Paint). Commonly applied on 2D grids.
# Given a 2D grid, replace all connected cells of the same original value starting from (sr, sc) with a new value.
def flood_fill(grid, sr, sc, new_color):
    rows, cols = len(grid), len(grid[0])
    original_color = grid[sr][sc]

    if original_color == new_color:
        return grid  # No change needed

    def dfs(r, c):
        # Boundary & color check
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] != original_color):
            return

        grid[r][c] = new_color

        # 4-directional neighbors
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return grid


grid = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

filled = flood_fill(grid, 1, 1, 2)

for row in filled:
    print(row)      # [2, 2, 2]
                    # [2, 2, 0]
                    # [2, 0, 1]