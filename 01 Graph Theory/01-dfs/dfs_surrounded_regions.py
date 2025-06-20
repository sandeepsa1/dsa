# Given a 2D board containing 'X' and 'O':
#   Capture all regions surrounded by 'X'.
#   A region is captured if it is completely surrounded by 'X'.
#   Flip all 'O's that are not on the border and not connected to border 'O's to 'X'.


def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] != 'O':
            return
        board[r][c] = '#'  # Mark safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Step 1: Mark all 'O's connected to borders
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Step 2: Flip internal 'O' to 'X', and '#' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

solve(board)

for row in board:
    print(''.join(row))     # XXXX
                            # XXXX
                            # XXXX
                            # XOXX