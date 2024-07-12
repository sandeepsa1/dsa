## Prim's algorithm
Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph. It greedily selects the vertex with the minimum key value and adds it to the MST, updating the key values of its adjacent vertices as necessary. This process continues until all vertices are included in the MST.
Prim's algorithm is not useful to find MST of disconnected graphs, where as Kruskal's algorithm can be used.
1. Time complexity:
   1. Using an adjacency list: O((V+E)logV)
   2. Using an adjacency matrix: 𝑂(𝑉<sup>2</sup>)
2. Space complexity:
   1. Using an adjacency list: O(V+E)
   2. Using an adjacency matrix: 𝑂(𝑉<sup>2</sup>)


### Uses
1. Network Design: It is commonly used in designing communication networks, such as telephone networks, computer networks, and transportation networks, to connect all nodes with the minimum cost.
2. Clustering: Prim's algorithm can be used in clustering applications, where the goal is to group similar data points together while minimizing the total distance or cost.
3. Approximation algorithms: It is often used as a subroutine in approximation algorithms for various optimization problems, such as the traveling salesman problem and facility location problems.
4. Routing protocols: In network routing protocols, Prim's algorithm can be used to construct routing tables or find optimal routes between network nodes.
5. Spanning tree applications: Minimum spanning trees have various applications in computer science and engineering, including in circuit design, image processing, and game theory.

### How it works
Prim's algorithm effectively grows the MST by starting from an arbitrary vertex and continuously adding the smallest edge that extends the MST until all vertices are included. It uses a priority queue to efficiently select the next smallest edge, ensuring the MST has the minimum total weight.</br>

1. Initialization:
   - Start with a single vertex (typically vertex 0).
   - Use a priority queue (min-heap) to store the edges connected to the MST, with their weights as the priority.
   - Mark the starting vertex as part of the MST and initialize the MST cost to 0.
2. Growing the MST(While there are still vertices not in the MST):
   - Extract the edge with the smallest weight from the priority queue.
   - If the vertex connected by this edge is not yet in the MST, add the edge to the MST.
   - Mark the new vertex as part of the MST and add the cost of the edge to the total MST cost.
   - Add all edges connected to this new vertex to the priority queue, if they lead to vertices not yet in the MST.
3. Show Minimum Spanning Tree as output