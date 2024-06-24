## Edmonds-Karp Algorithm Using Adjacency List
This project implements the Edmonds-Karp algorithm using an adjacency list to compute the maximum flow in a flow network. It computes the maximum flow in a flow network efficiently, making it suitable for large and sparse graphs.</br>

1. Time complexity: <b>𝑂(V⋅E<sup>2</sup>)</b>.
2. Space complexity: <b>𝑂(V + E)</b> using an adjacency list for graph representation.</br>


### Key Differences with Ford-Fulkerson algorithm
1. Path Finding Strategy:
   - <b>Ford-Fulkerson</b>: Can use any path-finding strategy (DFS, BFS, etc.).
   - <b>Edmonds-Karp</b>: Specifically uses BFS to find the shortest augmenting path.
2. Time Complexity:
   - <b>Ford-Fulkerson</b>: <b>O(max_flow⋅E)</b> with DFS; less predictable and can be exponential in the worst case.
   - <b>Edmonds-Karp</b>: <b>𝑂(V⋅E<sup>2</sup>)</b>; polynomial time complexity.
3. Efficiency:
   - <b>Ford-Fulkerson</b>: May require more iterations and can be less efficient due to the potential choice of longer augmenting paths.
   - <b>Edmonds-Karp</b>: More efficient due to BFS ensuring shortest augmenting paths, leading to fewer iterations.