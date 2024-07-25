## Maximum Spanning Tree (MaxST)
Kruskal's algorithm is used here to find the maximum spanning tree. The logic is exactly same as finding the minimum spanning tree. Only difference is that the edges are kept in decending order for processing.</br>
Time complexity     O(E log E)
Space complexity:   O(E + V)

### How it works
1. Sort Edges by Weight: In descending order
2. Initialize the forest: Initialize the MST as an empty forest (a set of trees), where each vertex is a separate tree.
3. Iterate Over Sorted Edges: For each edge:
   1. If the edge connects two different trees, add it to the MST and merge the trees.
   2. If the edge connects two vertices in the same tree, discard it (to avoid cycles).
4. Stop when MST is formed: Stop when there are V−1 edges in the MST (where V is the number of vertices).

### Uses
A maximum spanning tree (MaxST) is used in network design to maximize the total connection strength, ensuring the strongest possible links between nodes. It is also useful in clustering analysis where the goal is to maximize the intra-cluster distance, enhancing the separation between clusters. Additionally, MaxSTs are applied in optimizing resource allocation in distributed systems to ensure the most robust and efficient connectivity.