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
1. Initialize: Initialize an empty set to keep track of vertices included in the MST and an array key to store the minimum weight edge connecting a vertex to the MST.
2. Iterate Over all Vertices: For each vertex:
   1. Pick the vertex u which is not yet included in the MST and has the minimum key value.
   2. Add u to the MST by setting in_mst[u] = True.
   3. Update the key values of adjacent vertices of u if they are not in the MST and if the weight of the edge connecting them to u is less than their current key values.
3. Show Minimum Spanning Tree as output