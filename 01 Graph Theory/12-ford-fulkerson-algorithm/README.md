## Ford-Fulkerson Algorithm Using Adjacency List
This project implements the Ford-Fulkerson algorithm using an adjacency list to compute the maximum flow in a flow network. It computes the maximum flow in a flow network efficiently, making it suitable for large and sparse graphs.</br>

1. Time complexity: <b>𝑂(V⋅E<sup>2</sup>)</b> for the Edmonds-Karp implementation using BFS.
2. Space complexity: <b>𝑂(V + E)</b> using an adjacency list for graph representation.</br>


### Uses
1. Network Flow Analysis
   1. Optimizing data transfer in telecommunications and traffic flow in road networks.
2. Bipartite Matching
   1. Matching job applicants to jobs or students to colleges to maximize total matches.
3. Circulation with Demands
   1. Managing supply chains and water distribution systems to meet demand.
4. Image Segmentation
   1. Segmenting images into meaningful regions in computer vision applications.
5. Airline Scheduling
   1. Optimizing flight schedules for better resource utilization.

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

### How it works
1. Initialization:
   1. Start with zero flow in all edges.
2. Find Augmenting Path:
   1. Use a search algorithm (BFS in this case) to find a path from the source to the sink in the residual graph where every edge has a positive residual capacity.
3. Augment Flow:
   1. Determine the maximum amount of flow that can be sent along the augmenting path (this is the minimum residual capacity of the edges in the path).
   1. Increase the flow along the forward edges and decrease the flow along the backward edges of the augmenting path.
4. Update Residual Graph:
   1. Update the capacities in the residual graph to reflect the changes in flow.
5. Repeat:
   1. Repeat steps 2-4 until no more augmenting paths can be found.
6. Result:
   1. The flow values in the original network now represent the maximum flow from the source to the sink.

https://www.youtube.com/watch?v=3LG-My_MoWc