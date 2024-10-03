## Graph Traversal and Pathfinding Problems
Graph Traversal and Pathfinding Problems.

Samples included are;
1. <b>Number of Islands</b>: Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
2. <b>Shortest Path in Binary Matrix</b>: Given an n x n binary matrix, find the length of the shortest clear path from the top-left corner to the bottom-right corner.


### 1. Number of Islands
The problem of counting the number of islands in a 2D grid of '1's (land) and '0's (water) can be solved using graph traversal techniques like Depth-First Search (DFS) or Breadth-First Search (BFS). Each island is a group of connected '1's (vertically or horizontally connected).

1. Time complexity: <b>𝑂(n * m)</b>
2. Space complexity: <b>𝑂(n * m)</b>

#### Steps
1. Traverse the grid, cell by cell.
2. When you find a '1', it means you have encountered an unvisited part of an island.
3. Use DFS to mark all the connected '1's as visited by changing them to '0' or using a separate visited array.
4. Increment the island count and continue searching for more unvisited '1's.
5. Repeat until the entire grid is traversed.

### 2. Shortest Path in Binary Matrix
The "Shortest Path in a Binary Matrix" problem can be solved using Breadth-First Search (BFS), as BFS is ideal for finding the shortest path in an unweighted grid.

#### Steps
1. Use BFS to explore the shortest path level by level, starting from the top-left corner (0, 0).
2. Keep track of visited cells to avoid revisiting them.
3. For each cell, check its 8 possible neighbors (up, down, left, right, and four diagonals).
4. If you reach the bottom-right corner (n-1, n-1), return the current path length.
5. If the queue is exhausted without reaching the bottom-right, return -1 (no valid path exists).