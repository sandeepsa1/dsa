# Data Structures and Algorithms (DSA)
Welcome to the Data Structures and Algorithms repository! This repository contains code snippets and implementations of various algorithms across different topics.

#### Virtual Environment
The entire `dsa` folder is organized as a single virtual environment. You can either download the entire folder and run any code after activating the virtual environment using using command `scripts\activate`. Or download any sub folders and run it. In this case you may have to import some libraries.

## Table of Contents
- [Graph Theory](#graph-theory)
  - [01-dfs](#01-dfs)
  - [02-bfs](#02-bfs)
  - [03-dijkstras_algorithm](#03-dijkstras-algorithm)
  - [04-bellman-ford-algorithm](#04-bellman-ford-algorithm)
  - [05-floyd-warshall-algorithm](#05-floyd-warshall-algorithm)
  - [06-kruskal-algorithm](#06-kruskal-algorithm)
  - [07-prims-algorithm](#07-prims-algorithm)
  - [08-a-star-algorithm](#08-a-star-algorithm)
  - [09-topological-sort](#09-topological-sort)
  - [10-tarjans-algorithm](#10-tarjans-algorithm)
  - [11-johnsons-algorithm](#11-johnsons-algorithm)
  - [12-ford-fulkerson-algorithm](#12-ford-fulkerson-algorithm)
  - [13-edmonds-karp-algorithm](#13-edmonds-karp-algorithm)
  - [14-dinics-algorithm](#14-dinics-algorithm)
  - [15-hopcroft-karp-algorithm](#15-hopcroft-karp-algorithm)
  - [16-kosarajus-algorithm](#16-kosarajus-algorithm)
  - [17-kahns-algorithm](#17-kahns-algorithm)
  - [18-hungarian-algorithm](#18-hungarian-algorithm)
  - [19-viterbi-algorithm](#19-viterbi-algorithm)
  - [20-pagerank-algorithm](#20-pagerank-algorithm)
  - [21-second-shortest-path-unweighted-graph](#21-second-shortest-path-unweighted-graph)
  - [22-second-shortest-path-weighted-graph](#22-second-shortest-path-weighted-graph)
  - [23-second-best-spanning-tree](#23-second-best-spanning-tree)
  - [24-longest-path-unweighted-graph](#24-longest-path-unweighted-graph)
  - [25-longest-path-weighted-graph](#25-longest-path-weighted-graph)
  - [26-maximum-spanning-tree-kruskal](#26-maximum-spanning-tree-kruskal)
  - [27-minimum-cost-max-flow-using-sspa](#27-minimum-cost-max-flow-using-sspa)
- [Arrays](#arrays)
  - [01-search](#01-search)
  - [02-sort](#02-sort)
  - [03-two-pointer-technique](#03-two-pointer-technique)
  - [04-sliding-window-technique](#04-sliding-window-technique)
  - [05-divide-and-conquer](#05-divide-and-conquer)
  - [06-dynamic-programming](#06-dynamic-programming)
  - [07-matrix-manipulation-2d-arrays](#07-matrix-manipulation-2d-arrays)
  - [08-greedy-algorithms](#08-greedy-algorithms)


## Graph Theory

### 01-dfs
This section contains DFS algorithms and their various uses and variations, including traversal, path finding, topological sort, and spanning trees.

### 02-bfs
Here, you'll find BFS algorithms and their different applications, including traversal and shortest path finding.

### 03-dijkstras-algorithm
This folder contains code for Dijkstra's algorithm, used to find the shortest path in a weighted graph.

### 04-bellman-ford-algorithm
Bellman-Ford algorithm to find the shortest paths from a single source vertex to all other vertices in a weighted graph, including graphs with negative edge weights.

### 05-floyd-warshall-algorithm
Used to find the shortest paths between all pairs of vertices in a weighted graph, including graphs with negative edge weights (but with no negative cycles).

### 06-kruskal-algorithm
Kruskal's algorithm to find the minimum spanning tree of a weighted graph. Works for disconnected graphs also.

### 07-prims-algorithm
Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph.

### 08-a-star-algorithm
Finds the shortest path in a weighted graph with the help of a heuristic function. A* is generally more efficient than other algorithms with good heuristic.

### 10-tarjans-algorithm
Tarjan's Algorithm to find all strongly connected components (SCCs) in a directed graph.

### 11-johnsons-algorithm
Johnson's algorithm to find the shortest paths between all pairs of vertices in a weighted graph. Johnson's algorithm is particularly efficient for sparse graphs and works with negative weights, provided there are no negative weight cycles.

### 12-ford-fulkerson-algorithm
This project implements the Ford-Fulkerson algorithm using an adjacency list to compute the maximum flow in a flow network. It computes the maximum flow in a flow network efficiently, making it suitable for large and sparse graphs.

### 13-edmonds-karp-algorithm
Edmonds-Karp algorithm using an adjacency list to compute the maximum flow in a flow network. Difference with Ford-Fulkerson algorithm is the specific use of BFS in Edmonds-Karp algorithm to find the shortest augmenting paths, making this more efficient.

### 14-dinics-algorithm
Dinic's algorithm is an efficient algorithm for computing the maximum flow in a flow network. It uses a combination of Breadth-First Search (BFS) to construct level graphs and Depth-First Search (DFS) to send flow along these level graphs.

### 15-hopcroft-karp-algorithm
Hopcroft-Karp algorithm to find the maximum matching in a bipartite graph.

### 16-kosarajus-algorithm
Kosaraju's Algorithm to find all strongly connected components (SCCs) in a directed graph. Compared to Tarjan's Algorithm, this is relatively straightforward and easier to understand.

### 17-kahns-algorithm
Kahn's algorithm is used for topological sorting of a directed acyclic graph (DAG). It works by repeatedly removing nodes with no incoming edges and appending them to the topological order.

### 18-hungarian-algorithm
The Hungarian algorithm, also known as the Kuhn-Munkres algorithm, is used for solving the assignment problem, which involves finding the optimal way to assign n tasks that involves a cost(weight), to n agents such that the total cost is minimized.

### 19-viterbi-algorithm
The Viterbi algorithm is a dynamic programming algorithm used to find the most likely sequence of hidden states (also known as the Viterbi path) that results in a sequence of observed events, especially in the context of hidden Markov models (HMMs).

### 20-pagerank-algorithm
PageRank is an algorithm used to rank web pages in search engine results.

### 21-second-shortest-path-unweighted-graph
Find the second shortest path in an unweighted graph using BFS.

### 22-second-shortest-path-weighted-graph
Find the second shortest path in a weighted graph using Dijkstra's algorithm.

### 23-second-best-spanning-tree
Find the second-best spanning tree (SBST) of a graph.

### 24-longest-path-unweighted-graph
Find the longest path in an unweighted graph using DFS with memoization.

### 25-longest-path-weighted-graph
Find the longest path in a weighted graph using DFS with memoization.

### 26-maximum-spanning-tree-kruskal
Kruskal's algorithm to find the maximum spanning tree of a weighted graph.

### 27-minimum-cost-max-flow-using-sspa
Minimum Cost Maximum Flow algorithm using a basic implementation of the Successive Shortest Path Algorithm (SSPA) combined with Bellman-Ford to find shortest paths.


## Arrays

### 01-search
Implement array search algorithms.
  - Linear Search
  - Binary Search
  - Interpolation Search
  - Jump Search
  - Exponential Search

### 02-sort
Implement array sort algorithms.
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort

### 03-two-pointer-technique
Using Two Pointer Technique to solve;
  - Two Sum Problem
  - Three Sum Problem
  - K Sum Problem
  - Array Duplicate Removal
  - Container With Most Water

### 04-sliding-window-technique
The Sliding Window Technique is commonly used to solve problems involving subarrays, substrings, or other contiguous subsequences in arrays or strings. Here we see how to find:
  - Maximum Sum Subarray of Size K
  - Longest Substring Without Repeating Characters

### 05-divide-and-conquer
Divide and Conquer method is effective for a wide range of problems, including sorting, searching, and optimization. Two samples are implemented:
  - Finding the Closest Pair of Points which are kept as an array
  - Find K-th Largest Element in an array

### 06-dynamic-programming
Dynamic Programming (DP) is an algorithmic technique used for solving complex problems by breaking them down into simpler subproblems. Code implemented are:
  - Maximum Subarray Sum (Kadane’s Algorithm)
  - Longest Increasing Subsequence
  - Longest Common Subsequence

### 07-matrix-manipulation-2d-arrays
Matrix manipulation refers to a wide range of operations that can be performed on 2D arrays (also known as matrices). Implemented Matrix Manipulation Operations are:
  - Rotate n * n Matrix in 90, 180 or 270 Degrees
  - Spiral Order Traversal

### 08-greedy-algorithms
A greedy algorithm is an approach to solving optimization problems by making a series of decisions, each of which is locally optimal at the time. The idea is that by making the best possible choice at each step, the algorithm will ultimately arrive at a globally optimal solution. Some samples implemented:
  - Best Time to Buy and Sell Stock
  - Coin Change Problem