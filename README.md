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
Kruskal's algorithm to find a minimum spanning tree of a weighted graph. Works for disconnected graphs also.

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
Edmonds-Karp algorithm using an adjacency list to compute the maximum flow in a flow network. Difference with Ford-Fulkerson algorithm is the specific use of BFS to find the shortest augmenting paths, making Edmonds-Karp algorithm more efficient.