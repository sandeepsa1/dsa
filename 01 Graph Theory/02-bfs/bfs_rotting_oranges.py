from collections import deque

def oranges_rotting(grid):
    print(grid)


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print("Minutes until all oranges rot:", oranges_rotting(grid))