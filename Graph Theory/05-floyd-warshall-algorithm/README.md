## Floyd-Warshall algorithm
The Floyd-Warshall algorithm is a dynamic programming algorithm used to find the shortest paths between all pairs of vertices in a weighted graph, including graphs with negative edge weights (but with no negative cycles). It is an all-pairs shortest path algorithm, meaning it computes the shortest path between every pair of vertices in the graph.
The time complexity of the Floyd-Warshall algorithm is O(V^3). It is efficient for dense graphs or small graphs where the number of vertices is not very large.
Space complexity is O(V^2), which can be a limiting factor for large graphs.

### Uses
1. Shortest Path Problems: It is commonly used to find the shortest paths between all pairs of vertices in a weighted graph. This is useful in network routing protocols, such as OSPF (Open Shortest Path First) and IS-IS (Intermediate System to Intermediate System), where routers need to efficiently compute the shortest paths between all nodes in a network.
2. Traffic Engineering: In transportation and traffic engineering, the algorithm can be used to optimize traffic flow by finding the shortest paths between all pairs of locations on a road network. This helps in planning routes, estimating travel times, and minimizing congestion.
3. Network Analysis: Floyd-Warshall can be applied to analyze various types of networks, including social networks, communication networks, and supply chain networks. It helps in understanding the connectivity and relationships between different nodes in the network.
4. Resource Allocation: The algorithm can be used in resource allocation problems, such as minimizing the cost of transporting goods between multiple locations or optimizing the use of resources in a distributed system.

### How it works
1. Initialization: Create n * n matrix with all values as infinity. Set diagonal values to 0. Update all non-zero values to the matrix.
2. Iterative Updates: n iterations required. For each iteration a matrix is created like below.
Eg: For first iteration, first row and column and diagonal 0 of the intitial matrix is retained. Then for each node it check if there exists a shortest path along the first node using the below formula.
```python
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
If such path exists, the value is updated in the matrix.
Similarly for kth iteration, k<sup>th</sup> row and column and diagonal 0 of the (k-1)<sup>th</sup> matrix is retained. hen for each node it check if there exists a shortest path along the k<sup>th</sup> node, as explained above.
3. Handling Negative Cycles: After completing the iterations, the algorithm checks for negative cycles in the graph. A negative cycle occurs when the sum of the weights of the edges in a cycle is negative. If a negative cycle exists, it means that there is no shortest path between some pairs of vertices, as the path length can become increasingly negative by traversing the cycle repeatedly.
4. Output: The final output of the algorithm is a matrix containing the shortest distances between all pairs of vertices. If there is no path between two vertices, the corresponding distance in the matrix remains infinity.