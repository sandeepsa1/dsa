## Dijkstra's algorithm
Dijkstra's algorithm is a graph search algorithm used to find the shortest path between nodes in a weighted graph. The algorithm works by iteratively selecting the node with the smallest known distance from the source and updating the distances of its adjacent nodes.</br>
Dijkstra's algorithm can handle both directed and undirected graphs, but it requires non-negative edge weights. If the graph contains negative edge weights, other algorithms like Bellman-Ford may be more appropriate.</br>

1. Time complexity: O(V logV + E)
2. Space complexity: O(V + E)

### Uses
It's commonly used in many applications, including computer networking (routing protocols), GPS systems, and various optimization problems.

### How it works
1. Initialize distances: Assign a tentative distance of zero to the source node and infinity to all other nodes.
2. Create a priority queue (or use a min-heap) to keep track of nodes with the smallest tentative distance.
3. While there are still unvisited nodes:
   1. Select the unvisited node with the smallest tentative distance.
   1. For each neighbor of the current node:
      - Calculate the distance from the source to the neighbor through the current node.
      - If this distance is less than the neighbor's current tentative distance, update the neighbor's distance.
4. Mark the current node as visited.
5. Repeat until all nodes have been visited.

The algorithm terminates when all nodes have been visited, and the shortest distance to each node is identified.

https://www.youtube.com/watch?v=XB4MIexjvY0