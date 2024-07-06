## Kosaraju's Algorithm
Kosaraju's algorithm is a method for finding the strongly connected components (SCCs) of a directed graph.</br>
A strongly connected component of a directed graph is a maximal subgraph where every vertex is reachable from every other vertex within the subgraph.</br>

1. Time complexity: 𝑂(V + E)
2. Space complexity: 𝑂(V + E)</br>


### Uses
1. Finding SCCs in Web Crawlers
   1. Identify clusters of web pages that are highly interconnected.
2. Analyzing Networks
   1. Study social networks or biological networks to find clusters of nodes that are closely related.
3. Optimizing Compilers
   1. Decompose control flow graphs into SCCs for optimization.
4. Deadlock Detection
   1. Identify circular dependencies in resource allocation graphs.

### How it works
1. Step 1: DFS on Original Graph:
   - Perform a DFS on the original graph to determine the finishing times of each vertex. This creates a stack of vertices ordered by their finishing times.
2. Transpose the Graph:
   - Reverse the direction of all edges in the graph to obtain the transpose graph.
3. DFS on Transposed Graph:
   - Perform DFS on the transpose graph in the order defined by the stack from the first pass. Each DFS in this pass will discover one SCC.

### Comparison with Tarjan's Algorithm
1. Approach:
   - <b>Tarjan's</b>: Single-pass DFS. Use of low-link values.
   - <b>Kosaraju's</b>: Two-pass DFS with a transposition of the graph in between.
2. Ease of Implementation:
   - <b>Tarjan's</b>: More complex.
   - <b>Kosaraju's</b>: Relatively straightforward.
3. When to Use:
   - <b>Tarjan's</b>: More efficient in terms of space as it does not require transposing the graph. It is <b>ideal when minimizing space usage is crucial<.b>. However, it is more complex to implement due to the need to maintain and update low-link values and handle the stack correctly.
   - <b>Kosaraju's</b>: <b>Suitable when the graph representation can be easily transposed, and a straightforward implementation is preferred</b>. It is often easier to understand and implement due to its clear separation of the two DFS passes.

https://www.youtube.com/watch?v=R6uoSjZ2imo&t=11s