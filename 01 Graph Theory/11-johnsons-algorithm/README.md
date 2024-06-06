## Johnson's Algorithm for All-Pairs Shortest Paths
This repository contains implementation of Johnson's algorithm to find the shortest paths between all pairs of vertices in a weighted graph. Johnson's algorithm is particularly efficient for sparse graphs and works with negative weights, provided there are no negative weight cycles.</br>

1. Time complexity: O(V<sup>2</sup> * (E + VlogV))
2. Space complexity: O(V<sup>2</sup>)


### Uses
Johnson's algorithm, known for efficiently computing shortest paths between all pairs of vertices in a graph, finds applications in various domains including network analysis, software engineering (e.g., module dependency analysis), graph visualization, game development (e.g., pathfinding), operations research (e.g., optimization problems), bioinformatics, and data mining/machine learning (e.g., feature selection).

### How this works
Johnson's algorithm combines the Bellman-Ford algorithm and Dijkstra's algorithm to efficiently compute shortest paths in a graph. The main steps of the algorithm are:

1. **Add a new vertex `q`** connected to every other vertex with an edge weight of 0.
2. **Run Bellman-Ford** algorithm from `q` to find shortest path weights from `q` to all other vertices.
3. **Reweight the graph.** After running the Bellman-Ford algorithm, we obtain the shortest path distances from the new vertex to all other vertices. These distances are used to reweight the edges of the original graph. The reweighting process is as follows:
    1. For each edge (u, v) in the original graph, the weight of the edge is updated using the Bellman-Ford distances obtained earlier. The new weight is calculated as:</br>`new_weight = old_weight + h[u] - h[v]`, where `h[u]` and `h[v]` are the shortest path distances from the new vertex to vertices u and v, respectively.
    2. By adding or subtracting the difference in shortest path distances (`h[u] - h[v]`) to the original edge weights, we effectively reweight the edges of the graph such that all edge weights become non-negative. This step ensures that Dijkstra's algorithm, which requires non-negative edge weights, can be applied to find shortest paths efficiently.
4. **Run Dijkstra's algorithm** for each vertex in the reweighted graph.
5. **Adjust the final distances** to get the actual shortest path distances.

### Files
1. **johnson.py** contains steps to implement Johnson's algorithm.
2. **bellman_ford.py** contains Bellman-Ford algorithm steps. Same code as in folder `04-bellman-ford-algorithm`.
3. **dijkstra.py** contains Dijkstra algorithm steps. Same code as in folder `03-dijkstras-algorithm`.