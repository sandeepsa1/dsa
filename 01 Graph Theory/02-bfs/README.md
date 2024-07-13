## Breadht First Search (BFS)
1. bfs.py
   - Basic Breadth First Search algorithm

2. bfs_shortest_path.py
   - Use BFS to find shortest path


### Uses
1. Shortest Path Finding:
   - BFS can be used to find the shortest path between two nodes in an unweighted graph. It guarantees to find the shortest path if all edges have the same weight.
2. Finding Path:
   - BFS can be used to determine the connected components in an undirected graph. It can identify which vertices are reachable from a given starting vertex.
3. Crawl or Search Web Graphs:
   - BFS can be used to crawl or search web graphs by visiting web pages in a breadth-wise manner. It is the basis for web crawling algorithms used by search engines.
4. Finding Level in a Tree:
   - BFS can be used to find the level or depth of each node in a tree. Starting from the root node, BFS traverses each level of the tree before moving to the next level.
5. Finding the Diameter of a Tree:
   - BFS can be used to find the diameter of a tree, which is the longest path between any two nodes in the tree.
6. Finding Bipartite Graphs:
   - BFS can determine if a graph is bipartite by assigning a color to each node such that no two adjacent nodes have the same color. If BFS encounters a conflict during traversal, the graph is not bipartite.
7. Solving Puzzles and Games:
   - BFS can be used to solve puzzles and games with a finite number of states, such as the sliding puzzle, maze solving, and finding the shortest path in a game.