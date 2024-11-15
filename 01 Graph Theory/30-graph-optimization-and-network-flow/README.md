## Graph Optimization and Network Flow
Algorithms on Graph Optimization and Network Flow.

Samples included are;
1. <b>Network Delay Time</b>: There are N network nodes, labeled 1 to N. You are given a list of times where times[i] = (u, v, w) means the time it takes for a signal to travel from node u to node v is w seconds. Compute the time it takes for all nodes to receive a signal from a given start node.
2. <b>Critical Connections in a Network</b>: Given a network of n nodes and n-1 edges, find all critical connections (bridges) in the network.



### 1. Network Delay Time
This problem is known as the "Network Delay Time" problem and can be solved using Dijkstra’s Algorithm. The goal is to find the shortest time it takes for a signal to reach all nodes in a directed graph with weighted edges.

#### Steps
1. Graph Representation:
    - Use an adjacency list to represent the graph. Each entry in the adjacency list stores the destination node and the travel time as a tuple.
2. Shortest Path Algorithm:
    - Apply Dijkstra's Algorithm since it efficiently finds the shortest paths from a single source to all other nodes in a graph with non-negative weights.
    - Use a Min-Heap (Priority Queue) to always expand the shortest known path first.
3. Edge Cases:
    - If any node is unreachable, return -1.
    - If all nodes are reachable, return the maximum time it takes to reach any node.


### 2. Critical Connections in a Network
This problem is about finding critical connections (also known as bridges) in an undirected graph. A bridge in a graph is an edge that, if removed, would increase the number of connected components, effectively disconnecting the graph.

#### Steps
The most efficient way to find all the bridges in a graph is by using Tarjan's Algorithm. This algorithm uses Depth-First Search (DFS) and keeps track of discovery and low-link values to identify bridges.