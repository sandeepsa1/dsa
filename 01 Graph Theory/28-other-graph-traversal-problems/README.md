## Graph Traversal and Pathfinding Problems
Graph Traversal and Pathfinding Problems.

Samples included are;
1. <b>Number of Islands</b>: Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
2. <b>Shortest Path in Binary Matrix</b>: Given an n x n binary matrix, find the length of the shortest clear path from the top-left corner to the bottom-right corner.
3. <b>Longest Path in a Matrix</b>: Given an m x n matrix of integers, find the length of the longest increasing path in the matrix.
4. <b>The Maze</b>: Given a maze represented as a 2D grid, find the shortest path from the start to the destination.
5. <b>Clone Graph</b>: Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.
6. <b>Word Ladder</b>: Given two words (start and end) and a dictionary, find the length of the shortest transformation sequence from start to end.
7. <b>Reconstruct Itinerary</b>: Given a list of airline tickets represented as pairs of departure and arrival airports, reconstruct the itinerary in order.
8. <b>Alien Dictionary</b>: Given a list of words from the alien language, determine the order of characters in the alien language.


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

### 3. Longest Path in a Matrix
The problem of finding the Longest Path in a Matrix involves determining the maximum length of a path such that the values in the matrix strictly increase along the path.

#### Steps
1. DFS with Memoization:
    - For each cell (i, j) in the matrix, perform DFS to find the longest increasing path starting from that cell.
    - During the DFS, check the neighbors (up, down, left, right). If the neighbor has a larger value, move to that cell and continue the DFS.
    - Use a memoization table dp where dp[i][j] stores the result of the longest increasing path starting from cell (i, j).
2. Memoization:
    - If the result for a cell is already computed, return the stored value to avoid redundant DFS calls.
3. Edge Cases:
    - If the matrix is empty, return 0.
    - If all elements are the same, the longest path will be 1 (no increase).

### 4. The Maze
To solve the problem of finding the shortest path in a maze represented as a 2D grid, use Breadth-First Search (BFS). BFS is ideal for this type of problem because it explores all possible paths in layers and guarantees that the first time a destination is reached, it is via the shortest path.

#### Steps
1. Initialize a queue and add the starting point with 0 steps.
2. Initialize a visited array to keep track of the cells that have already been visited.
3. Perform BFS, exploring the 4 possible directions (up, down, left, right).
4. If you reach the destination, return the number of steps taken.
5. If the queue is exhausted and the destination is not reached, return -1.

### 5. Clone Graph
To clone a connected undirected graph, traverse the original graph and make a deep copy of every node and its edges. A common approach to this problem is using either Depth-First Search (DFS) or Breadth-First Search (BFS) algorithm.

#### Steps
1. If the node has already been visited, return its clone.
2. If the node hasn't been visited, create a clone and recursively clone its neighbors.

### 6. Word Ladder
To solve the problem of finding the shortest transformation sequence from a start word to an end word by changing one letter at a time, where each transformed word must be present in a given dictionary (or word list), Breadth-First Search can be used. BFS is suitable here because it finds the shortest path in an unweighted graph, where each word represents a node, and edges represent valid one-letter transformations.

#### Steps
1. Breadth-First Search (BFS):
    - Treat each word as a node in a graph. Use BFS to explore all possible transformations level by level, ensuring you get the shortest path.
2. Queue:
    - Maintain a queue where each entry is a tuple (current word, current length of transformation sequence).
3. Visited Set:
    - Track the words that have already been visited to avoid revisiting and infinite loops.
4. Word Pattern Matching:
    - For each word, generate all possible intermediate words by replacing each letter with * (wildcard), and use these patterns to quickly find neighbors (words that differ by one letter).

### 7. Reconstruct Itinerary
The problem of reconstructing an itinerary from a list of airline tickets can be solved using Depth-First Search (DFS), given the constraints that the itinerary must follow the lexicographically smallest order when multiple airports are possible.

#### Steps
1. Graph Representation:
    - Model the tickets as a directed graph where each airport is a node, and each ticket is a directed edge from the departure airport to the arrival airport.
2. DFS with Lexicographic Order:
    - Use DFS to construct the itinerary. Since multiple tickets may exist from a single airport, explore them in lexicographically smallest order, meaning the destinations need to be sorted.
3. Hierholzer's Algorithm (Postorder DFS for Eulerian Path):
    - Since all edges to be visited exactly once (each ticket is used exactly once), this is similar to finding an Eulerian path. Use post-order DFS and add airports to the result list once we've used all tickets from a specific airport.

### 8. Alien Dictionary
The problem of reconstructing an itinerary from a list of airline tickets can be solved using Depth-First Search (DFS), given the constraints that the itinerary must follow the lexicographically smallest order when multiple airports are possible.

#### Steps
1. Build a graph from the list of words by comparing adjacent words and adding directed edges based on character order.
2. Perform topological sorting using BFS (Kahn’s Algorithm) or DFS.
3. If the topological sort is valid, return the character order. Otherwise, return an empty string.