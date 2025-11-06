# Given an m x n board representing a Minesweeper game.
# Each cell can be:
#   'M' → mine
#   'E' → unrevealed empty cell
#   'B' → revealed blank cell (0 adjacent mines)
#   '1'–'8' → number of adjacent mines
# 'X' → mine clicked (game over)
# When a cell is clicked:
#   If it’s a mine, it becomes 'X'.
#   If it’s an empty cell with adjacent mines → show the count.
#   If it’s an empty cell with no adjacent mines, reveal it as 'B' and recursively reveal all its neighbors (BFS/DFS).


from collections import deque

def updateBoard(board, click):
    rows, cols = len(board), len(board[0])
    r, c = click

    # If mine clicked
    if board[r][c] == 'M':
        board[r][c] = 'X'
        return board

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def count_adjacent_mines(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                count += 1
        return count

    queue = deque([click])

    while queue:
        r, c = queue.popleft()
        if board[r][c] != 'E':
            continue  # already revealed

        mines = count_adjacent_mines(r, c)
        if mines > 0:
            board[r][c] = str(mines)
        else:
            board[r][c] = 'B'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'E':
                    queue.append((nr, nc))

    return board


board = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
]

click = [3, 0]

new_board = updateBoard(board, click)

for row in new_board:
    print(row)                          # ['B', '1', 'E', '1', 'B']
                                        # ['B', '1', 'M', '1', 'B']
                                        # ['B', '1', '1', '1', 'B']
                                        # ['B', 'B', 'B', 'B', 'B']