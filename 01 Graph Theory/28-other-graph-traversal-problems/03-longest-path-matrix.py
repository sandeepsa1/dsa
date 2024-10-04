def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row, col):
        if dp[row][col] != -1:
            return dp[row][col]

        max_length = 1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_length = max(max_length, 1 + dfs(new_row, new_col))

        dp[row][col] = max_length
        return dp[row][col]

    longest_path = 0
    for i in range(rows):
        for j in range(cols):
            longest_path = max(longest_path, dfs(i, j))

    return longest_path


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

print("Longest Increasing Path Length:", longestIncreasingPath(matrix))  # 4