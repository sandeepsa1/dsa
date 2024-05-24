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
   1. Initialize id to 0.
   1. Initialize arrays ids, low, sccs, and visited.
   1. Initialize an empty stack.
   1. Set all vertices' ids to -1 to indicate they are unvisited.
2. Main Loop:
   1. For each vertex, if it is unvisited, perform a DFS from that vertex.
3. DFS Function:
   1. Set the id and low-link value of the current vertex to id.
   1. Increment id.
   1. Push the vertex onto the stack and mark it as visited.
   1. For each adjacent vertex, if it is unvisited, recursively perform a DFS on it, then update the current vertex's low-link value. If the adjacent vertex is on the stack, update the low-link value with the adjacent vertex's id.
   1. After visiting all adjacent vertices, if the id of the current vertex equals its low-link value, it indicates the start of an SCC. Pop vertices from the stack until the current vertex is reached, assigning them to the same SCC.