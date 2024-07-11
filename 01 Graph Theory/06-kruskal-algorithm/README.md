## Kruskal algorithm
Kruskal's algorithm iteratively adds the smallest edge that does not form a cycle, until all vertices are connected. This results in a minimum spanning tree that spans all vertices of the original graph while minimizing the total edge weight.
Kruskal's algorithm may be used to find MST of disconnected graphs, where as Prim's algorithm cannot be used in this situation.
Time complexity     O(E log E)
Space complexity:   O(E + V)

### Uses
1. Network Design: It is commonly used in designing communication networks, such as telephone networks, computer networks, and transportation networks, to connect all nodes with the minimum cost.
2. Circuit Design: To find the minimum-cost spanning tree for connecting components in a circuit.
3. Cluster Analysis: It can be applied to cluster analysis in data mining and machine learning, where it helps identify the most important relationships or connections between data points.
4. Image Segmentation: Kruskal's algorithm can be utilized in image processing and computer vision to segment images into regions based on similarity or connectivity.
5. Minimum Cost Problem: It is useful in solving various minimum-cost problems, such as finding the minimum-cost path in transportation or logistics networks.

### How it works
1. Sort Edges by Weight: In ascending order
2. Initialize the forest: Initialize the MST as an empty forest (a set of trees), where each vertex is a separate tree.
3. Iterate Over Sorted Edges: For each edge:
   1. If the edge connects two different trees, add it to the MST and merge the trees.
   2. If the edge connects two vertices in the same tree, discard it (to avoid cycles).
4. Stop when MST is formed: Stop when there are V−1 edges in the MST (where V is the number of vertices).

### Key Concept
1. Disjoint Set (Union-Find):
A Disjoint Set (or Union-Find) data structure is used to keep track of which vertices are in which components (trees). This helps in efficiently checking if two vertices are in the same tree and merging trees. It is a combination of 2 primary operations:
   - <b>Find</b>: Determine which subset a particular element is in. This can be used to check if two elements are in the same subset.
   - <b>Union</b>: Join two subsets into a single subset.