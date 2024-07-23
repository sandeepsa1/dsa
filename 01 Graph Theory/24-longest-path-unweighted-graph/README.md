## Longest path in an unweighted graph
To find the longest path in an unweighted graph, depth-first search (DFS) approach with memoization can be used.</br>

1. Time complexity: <b>𝑂(V + E)</b>
2. Space complexity: <b>𝑂(V<sup>2</sup>)</b></br>


### How this works
1. The 'dfs' function performs a depth-first search from the current node to the end node, keeping track of the current path.
2. If the current node is the end node, it returns the current path.
3. If the current node is already in the memoization dictionary 'memo', it returns the precomputed longest path from this node.
4. Otherwise, it explores each neighbor, recursively calling dfs and updating the longest path found.
5. The memoization dictionary stores the longest path from each node to the end node, avoiding redundant calculations.

### Uses
Finding the longest path in a graph is essential in various fields, such as project scheduling, where it helps identify the critical path in a project timeline. It is also used in network optimization to determine the maximum delay path in communication networks, ensuring reliability and robustness in data transmission.


### Memoization
Memoization is an optimization technique used primarily to improve the efficiency of recursive algorithms. It involves storing the results of expensive function calls and reusing the cached result when the same inputs occur again.

#### Key Concepts of Memoization
1. Caching:
    - Memoization involves caching or storing the results of function calls. When a function is called with specific arguments, the result is saved in a cache (usually a dictionary or array).
2. Avoid Redundant Calculations:
    - By reusing the cached results for the same inputs, memoization avoids redundant calculations. This is especially useful for problems with overlapping subproblems, where the same subproblems are solved multiple times.
3. Trade-off:
    - Memoization trades increased space usage for decreased time complexity. It uses additional memory to store intermediate results but significantly reduces the number of computations.

#### Benefits of Memoization
1. Efficiency:
    - Reduces the time complexity from exponential (without memoization) to linear (with memoization) for the Fibonacci example.
2. Simplicity:
    - Easy to implement and integrate into existing recursive algorithms.
3. Reusability:
    - Cached results can be reused across multiple function calls.