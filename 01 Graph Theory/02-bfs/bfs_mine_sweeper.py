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
