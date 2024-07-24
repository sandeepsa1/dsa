## Tarjan's Algorithm
Tarjan's Algorithm is a depth-first search (DFS)-based method used to find all strongly connected components (SCCs) in a directed graph. An SCC is a maximal subgraph where every pair of vertices is mutually reachable.</br>
https://www.youtube.com/watch?v=wUgWX0nc4NY

1. Time complexity: 𝑂(V + E)
2. Space complexity: 𝑂(V + E)</br>

These complexities make Tarjan's Algorithm very efficient for finding strongly connected components in directed graphs, particularly suitable for large sparse graphs where the number of edges is close to the number of vertices.


### Uses
1. Compiler Optimization
   1. Control Flow Analysis: Identifies code regions for optimization.
   2. Interprocedural Analysis: Optimizes function calls.
2. Graph Theory
   1. Condensation Graph: Simplifies graph structure by contracting SCCs into single vertices.
3. Circuit Analysis
   1. Electronic Circuits: Detects feedback loops to ensure stability.
4. Database Systems
   1. Dependency Analysis: Finds cycles in dependency graphs.
   2. Query Optimization: Reorders operations to minimize dependencies.
5. Deadlock Detection
   1. Operating Systems: Identifies deadlocks in resource allocation.
6. Web Crawling
   1. Website Analysis: Clusters interconnected web pages for better understanding.
7. Social Network Analysis
   1. Community Detection: Finds highly interconnected user groups.

### How it works
1. Initialization:
   1. <b>index</b>: A counter to uniquely identify the order of visitation.
   1. <b>stack</b>: Used to store the vertices of the current SCC.
   1. <b>indices</b>: Stores the index at which each node is first visited.
   1. <b>lowlink</b>: Stores the smallest index reachable from the node.
   1. <b>on_stack</b>: Tracks whether a node is on the stack.
   1. <b>sccs</b>: List of SCCs.
2. DFS Helper Function (<b>strongconnect</b>):
   1. Assigns an index to the node 'v' and pushes it onto the stack.
   1. Recursively visits all unvisited neighbors ('w') and updates the 'lowlink' value of 'v'.
   1. If 'w' is on the stack, it updates the 'lowlink' value of 'v' to the minimum of 'lowlink[v]' and 'indices[w]'.
   1. If 'v' is a root node (i.e., 'lowlink[v] == indices[v]'), it pops all nodes from the stack until 'v' is reached, forming an SCC.
2. Main Function:
   1. Iterates through all nodes in the graph and calls the 'strongconnect' function for each unvisited node.