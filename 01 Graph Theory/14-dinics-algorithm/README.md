## Dinic's algorithm Using Adjacency List
Dinic's algorithm is an efficient algorithm for computing the maximum flow in a flow network. It uses a combination of Breadth-First Search (BFS) to construct level graphs and Depth-First Search (DFS) to send flow along these level graphs.</br>

1. Time complexity: <b>𝑂(V<sup>2</sup>.E)</b> for general graphs.
2. Space complexity: <b>𝑂(V + E)</b>.</br>


### Key Differences with Edmonds-Karp algorithm
1. Path Finding Strategy:
   - <b>Edmonds-Karp</b>: Specifically uses BFS to find the shortest augmenting path.
   - <b>Dinic's</b>: Constructs a level graph using BFS to identify layers of nodes. Uses DFS to find blocking flows within the level graph.
2. Time Complexity:
   - <b>Edmonds-Karp</b>: <b>𝑂(V⋅E<sup>2</sup>)</b>; polynomial time complexity.
   - <b>Dinic's</b>: <b>𝑂(V<sup>2</sup>.E)</b> for general graphs.
3. Efficiency:
   - <b>Edmonds-Karp</b>: Simple and easy to implement. Practical for small to medium-sized networks but can be inefficient for large, dense networks.
   - <b>Edmonds-Karp</b>: More efficient for larger and more complex networks. Handles large graphs better due to its structured approach with level graphs and blocking flows.

### Key Concepts
1. Flow Network:
   - A directed graph where each edge has a capacity and each edge receives a flow.
   - The amount of flow on an edge cannot exceed the capacity of the edge.
   - Typically, a source node (s) where the flow originates and a sink node (t) where the flow is collected.
2. Residual Graph:
   - Constructed from the original flow network.
   - Shows the available capacity on each edge after considering the current flow.
   - Contains forward edges (original direction) and backward edges (reverse direction for potential cancellation of flow).
3. Augmenting Path:
   - A path from the source to the sink in the residual graph where the available capacity is greater than zero on all edges in the path.
   - Used to increase the overall flow in the network.
4. Level Graph:
   - A level graph is a subgraph of the residual graph.
   - It assigns levels to each node. The source node is at level 0. Any node that is reachable from the source node in one edge is at level 1. Any node that is reachable from the source node in two edges is at level 2, and so on.
   - In Dinic's algorithm, BFS is used to find the level graphs.

### How it works
1. Initialization:
   1. Start with zero flow in the network.
2. Construct Level Graph Using BFS:
   1. Perform a BFS from the source (A) to the sink (F).
   1. The level graph only includes edges where the destination node's level is one more than the source node's level, and there is positive residual capacity.
3. Send Flow Using DFS:
   1. Use DFS to find blocking flows in the level graph and update residual capacities.
   1. Start from the source A and attempt to send flow to the sink F. Example DFS path from A to F: A -> B -> D -> F.
4. Repeat Until No Augmenting Path Exists:
   1. Repeat the BFS to construct a new level graph.
   1. Perform DFS to find new blocking flows.
If no more augmenting paths are found, the algorithm terminates.

https://www.youtube.com/watch?v=M6cm8UeeziI