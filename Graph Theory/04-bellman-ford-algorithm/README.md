## Bellman-Ford algorithm
Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph, including graphs with negative edge weights. It is particularly useful in scenarios where Dijkstra's algorithm cannot be applied due to the presence of negative edge weights.

### Uses
1. Network routing: Finding the shortest path between two nodes in a computer network.
2. Traffic planning: Determining the shortest route between two locations in a road network, considering factors such as traffic congestion and road closures.
3. Flight scheduling: Optimizing flight routes to minimize travel time and costs between airports.
4. Telecommunication networks: Routing data packets efficiently through a network of routers to minimize delays and congestion.

### How it works
1. Initialization: Initialize the distance to all vertices from the source vertex as infinity, except for the source vertex itself, which is initialized to 0.
2. Relaxation: Repeat the relaxation process for |V| - 1 times, where |V| is the number of vertices in the graph. During each iteration, iterate through all the edges in the graph and update the distance to each vertex if a shorter path is found.
3. Checking for Negative Cycles: After performing relaxation for |V| - 1 times, check for the presence of negative-weight cycles. If, during the final iteration, any relaxation operation results in a shorter distance, it indicates the presence of a negative-weight cycle.
4. Updating Distances in Negative Cycles: If a negative-weight cycle is detected, update the distances of vertices in the cycle to negative infinity.
5. Output: The final distances computed after the relaxation process represent the shortest distances from the source vertex to all other vertices in the graph.