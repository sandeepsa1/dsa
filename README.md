# Data Structures and Algorithms (DSA)
Welcome to the Data Structures and Algorithms repository! This repository contains code snippets and implementations of various algorithms across different topics.

#### Virtual Environment
The entire `dsa` folder is organized as a single virtual environment. You can either download the entire folder and run any code after activating the virtual environment using using command `scripts\activate`. Or download any sub folders and run it. In this case you may have to import some libraries.

## Table of Contents
<details>
  <summary>1. Graph Theory</summary>
    
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
  - [28-other-graph-traversal-problems](#28-other-graph-traversal-problems)
  - [29-cycle-detection-sort-and-graph-properties](#29-cycle-detection-sort-and-graph-properties)
  - [30-graph-optimization-and-network-flow](#30-graph-optimization-and-network-flow)
  - [31-graph-representations-conversion](#31-graph-representations-conversion)
</details>

<details>
  <summary>2. Arrays</summary>
  
  - [01-search](#01-search)
  - [02-sort](#02-sort)
  - [03-two-pointer-technique](#03-two-pointer-technique)
  - [04-sliding-window-technique](#04-sliding-window-technique)
  - [05-divide-and-conquer](#05-divide-and-conquer)
  - [06-dynamic-programming](#06-dynamic-programming)
  - [07-matrix-manipulation-2d-arrays](#07-matrix-manipulation-2d-arrays)
  - [08-greedy-algorithms](#08-greedy-algorithms)
  - [09-important-coding-problems](#09-important-coding-problems)
</details>

<details>
  <summary>3. Strings</summary>
  
  - [01-pattern-matching](#01-pattern-matching)
  - [02-substring-problems](#02-substring-problems)
  - [03-dynamic-programming](#03-dynamic-programming)
  - [04-string-transformations](#04-string-transformations)
  - [05-trie-based-algorithms](#05-trie-based-algorithms)
  - [06-important-coding-problems](#06-important-coding-problems)
</details>

<details>
  <summary>4. Linked Lists</summary>
  
  - [01-basic-operations](#01-basic-operations)
  - [02-clone-merge-partition-flattening-intersection](#02-clone-merge-partition-flattening-intersection)
  - [03-cycle-detection-find-kth-element](#03-cycle-detection-find-kth-element)
  - [04-sort-reverse-split-reorder-rotate](#04-sort-reverse-split-reorder-rotate)
  - [05-important-coding-problems](#05-important-coding-problems)
</details>

<details>
  <summary>5. Stacks</summary>
  
  - [01-stack-basic-operations](#01-stack-basic-operations)
  - [02-important-coding-problems](#02-important-coding-problems)
</details>

<details>
  <summary>6. Queues</summary>
  
  - [01-queue-basic-operations](#01-queue-basic-operations)
  - [02-important-coding-problems-queue](#02-important-coding-problems-queue)
</details>

<details>
  <summary>7. Trees</summary>
  
  - [01-traversal](#01-traversal)
  - [02-binary-search-tree](#02-binary-search-tree)
  - [03-lowest-common-ancestor](#03-lowest-common-ancestor)
  - [04-tree-properties-and-checks](#04-tree-properties-and-checks)
  - [05-tree-construction-and-transformation](#05-tree-construction-and-transformation)
  - [06-special-algorithms-and-operations](#06-special-algorithms-and-operations)
</details>

<details>
  <summary>8. Hash Tables</summary>
  
  - [01-basic-hash-table-operations](#01-basic-hash-table-operations)
  - [02-frequency-and-duplicates](#02-frequency-and-duplicates)
  - [03-subarray-and-substring-problems](#03-subarray-and-substring-problems)
  - [04-anagram-and-isomorphic-problems](#04-anagram-and-isomorphic-problems)
  - [05-with-multiple-arrays](#05-with-multiple-arrays)
</details>

<details>
  <summary>09 Sets and Maps</summary>
  
  - [01-set-operations](#01-set-operations)
  - [02-dictionary-operations](#02-dictionary-operations)
</details>


## 1. Graph Theory

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

### 28-other-graph-traversal-problems
Graph Traversal and Pathfinding Problems.
  - Number of Islands
  - Shortest Path in Binary Matrix
  - Longest Path in a Matrix
  - The Maze
  - Clone Graph
  - Word Ladder
  - Reconstruct Itinerary
  - Alien Dictionary

### 29-cycle-detection-sort-and-graph-properties
Cycle Detection, Topological Sorting, and Graph Properties.
  - Graph Coloring
  - DFS-Based Cycle Detection
  - Union-Find Based Cycle Detection
  - Find the Town Judge
  - Minimum Height Trees
  - Number of Connected Components in an Undirected Graph
  - Course Schedule

### 30-graph-optimization-and-network-flow
  - Network Delay Time
  - Critical Connections in a Network

### 31-graph-representations-conversion
  - Adjacency Matrix to Adjacency List
  - Adjacency Matrix to Edge List
  - Adjacency List to Adjacency Matrix
  - Adjacency List to Edge List
  - Edge List to Adjacency List
  - Edge List to Adjacency Matrix


## 2. Arrays

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

### 09-important-coding-problems
Some of the important and most common coding problems related to Arrays Data Structure.
  - Product of Array Except Self
  - Maximum Product Subarray
  - Find Minimum in Rotated Sorted Array
  - Search in Rotated Sorted Array
  - Merge Intervals


## 3. Strings

### 01-pattern-matching
String pattern matching algorithms are techniques used to find occurrences of a "pattern" within a "text" . These algorithms are fundamental in various applications, including text editors, search engines, DNA sequencing, and more. Following pattern matching algorithms are implemented:
  - Naive Pattern Matching
  - Knuth-Morris-Pratt (KMP)
  - Rabin-Karp
  - Boyer-Moore (Most efficient among these)

### 02-substring-problems
A substring is a contiguous sequence of characters within a string. Substring problems find, manipulate, or analyze substrings within a larger string. These problems are common in various domains, including text processing, bioinformatics, data compression, and more.
  - Longest Common Substring
  - Longest Palindromic Substring

### 03-dynamic-programming
Dynamic Programming (DP) to solve string related problems.
  - Longest Common Subsequence
  - Compute the Minimum Number of Operations to Transform One String into Another

### 04-string-transformations
String transformation generally refers to the process of converting one string into another, converting string to integer or vice versa, changing case, etc.
  - String to Integer (atoi)
  - Integer to String (itoa)

### 05-trie-based-algorithms
Trie-based algorithms uses a data structure called a Trie or prefix tree to efficiently store and retrieve strings, typically used for solving problems related to searching, prefix matching, and autocomplete functionalities.
  - Trie Construction
  - Autocomplete
  - Longest Common Prefix

### 06-important-coding-problems
Some of the important and most common coding problems related to Strings.
  - Anagram Check
  - Group Anagrams
  - Count and Say
  - Z-Algorithm
  - Valid Parentheses
  - Minimum Window Substring
  - Zigzag Conversion


## 4. Linked Lists
  
### 01-basic-operations
Basic Linked List operations.
  - Traversal
  - Insert/Update/Delete
  - Reverse a Linked List
  - Check if a Linked List is a Palindrome

### 02-clone-merge-partition-flattening-intersection
Clone, Merge, Flattening, Partition and Intersection of Linked Lists
  - Clone a Linked List with Random Pointers
  - Merge Two Sorted Lists
  - Merge K Sorted Lists
  - Partition List
  - Flatten a Multilevel Doubly Linked List
  - Find Intersection Node

### 03-cycle-detection-find-kth-element
Cycle Detection and find Kth Element
  - Detect a Cycle and Find the Starting Node of the Cycle
  - Find Kth to Last Element

### 04-sort-reverse-split-reorder-rotate
Sort, Reverse, Split, Reorder and Rotate operations of Linked Lists
  - Sort List
  - Remove Duplicates from Sorted List
  - Reverse Nodes in k-Group
  - Split Linked List in Parts
  - Reorder List
  - Rotate List

### 05-important-coding-problems
Some of the important and most common coding problems related to Linked Lists.
  - Add Two Numbers
  - Swap Nodes in Pairs
  - Odd Even Linked List


## 05. Stacks

### 01-stack-basic-operations
Basic Stack operations.
  - Push, Pop, Peek, IsEmpty
  - Sort a Stack
  - Reverse a String
  - Evaluate Reverse Polish Notation
  - Min Stack
  - Infix to Postfix Conversion
  - Evaluate Postfix Expression

### 02-important-coding-problems
Some of the important and most common coding problems related to Stacks.
  - Next Greater Element - One Array
  - Next Greater Element - Two Arrays
  - Stock Span Problem
  - Daily Temperatures
  - Largest Rectangle in Histogram
  - Trapping Rain Water


## 06. Queues

### 01-queue-basic-operations
Basic Queue operations.
  - Enqueue, Dequeue, Front, isEmpty
  - Circular Queue
  - Queue using Stacks
  - Generate Binary Numbers
  - Level Order Traversal of Binary Tree

### 02-important-coding-problems-queue
Some of the important and most common coding problems related to Queues.
  - Sliding Window Maximum
  - LRU Cache
  - Rotten Oranges
  - Moving Average from Data Stream
  - Number of Recent Calls
  - Course Schedule


## 7. Trees

### 01-traversal
Implement tree traversal algorithms.
  - Inorder Traversal
  - Preorder Traversal
  - Postorder Traversal
  - Level Order Traversal
  - Non-Binary Tree Traversal

### 02-binary-search-tree
  - Insert, Update, Delete
  - Search
  - Binary Search Tree Iterator
  - Kth Smallest Element in a BST
  - Minimum Distance Between BST Nodes

### 03-lowest-common-ancestor
  - LCA of a Binary Tree
  - LCA of a Binary Search Tree

### 04-tree-properties-and-checks
  - Height of a Tree
  - Diameter of a Tree
  - Diameter of Binary Tree
  - Maximum Depth of Binary Tree
  - Balanced Tree Check
  - Check for Symmetry
  - Sum of Left Leaves

### 05-tree-construction-and-transformation
  - Convert BST to Sorted Doubly Linked List
  - Convert Sorted Array to Binary Search Tree
  - Invert Binary Tree
  - Construct Binary Tree from Preorder and Inorder Traversal

### 06-special-algorithms-and-operations
  - Find Path Sum
  - Find Duplicate Subtrees
  - Recover Binary Search Tree
  - Tree to String - Serialize and Deserialize


## 8. Hash Tables

### 01-basic-hash-table-operations
  - Insert, Update, Delete, Search
  - Hash Functions
  - Rehashing

### 02-frequency-and-duplicates
  - Counting Frequencies
  - Finding Duplicates
  - Top K Frequent Elements
  - First Unique Character in a String

### 03-subarray-and-substring-problems
  - Subarray with Sum Zero
  - Contiguous Array

### 04-anagram-and-isomorphic-problems
  - Find All Anagrams in a String
  - Isomorphic Strings
  - Minimum Index Sum of Two Lists

### 05-with-multiple-arrays
  - Happy Number
  - Intersection of Two Arrays
  - Longest Consecutive Sequence
  - Four Sum II


## 9. Sets and Maps

### 01-set-operations
  - Union, Intersection, Difference
  - Symmetric Difference of Sets, Subset Check, Superset Check, Set Comprehensions

### 02-dictionary-operations
  - Insert, Update, Delete, Check
  - Fetch Values and Iterations
  - Merge Dictionaries
  - Default and Ordered Dictionaries