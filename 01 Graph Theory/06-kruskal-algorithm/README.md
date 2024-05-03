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
2. Iterate Over Sorted Edges: For each edge:
i. Check if adding the edge to the MST forms a cycle. This is done by finding parent nodes of (u, v). For example in the given graph, on the third iteration (0, 2, 6) is considered. If we iteratively find the parent node of 0 or 2, at some point, we will get x == y (2 == 2). So this is a cycle. We skip this edge.
ii. If adding the edge does not create a cycle, add it to the MST.
3. Show Minimum Spanning Tree as output

1. Item 1
   1. Sub-item 1.1
   2. Sub-item 1.2
2. Item 2
   1. Sub-item 2.1
   2. Sub-item 2.2
