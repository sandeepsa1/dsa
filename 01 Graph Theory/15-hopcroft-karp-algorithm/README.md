## Hopcroft-Karp Algorithm
An unweighted bipartite matching algorithm is used to find the maximum matching in a bipartite graph. One of the most common algorithms for this task is the Hopcroft-Karp algorithm.</br>

A bipartite graph is a graph whose vertices can be divided into two disjoint sets <b>u</b> and <b>v</b> such that every edge connects a vertex in <b>u</b> to a vertex in <b>v</b>.

1. Time complexity: <b>𝑂(√V * E)</b>.
2. Space complexity: <b>𝑂(V + E)</b>.</br>


### Key Concepts
1. <b>Matching</b>: A matching in a graph is a set of edges such that no two edges share a common vertex.
2. <b>Maximum Matching</b>: A matching that contains the largest possible number of edges.
3. <b>Perfect Matching</b>: A matching that matches all vertices of the graph.
4. <b>Level Graph</b>: A level graph is a subgraph of the original bipartite graph where vertices are assigned levels based on their distance from the unmatched vertices in the left set U.The level graph only includes edges that connect vertices on consecutive levels.
5. <b>Augmenting Path</b>: An augmenting path starts at an unmatched vertex in U and ends at an unmatched vertex in V. It alternates between edges that are not in the current matching and edges that are in the current matching.

### How it works
1. Level Graph Construction (BFS):
   - Perform a breadth-first search (BFS) starting from all unmatched vertices in set <b>u</b>.
   - Assign levels to the vertices. Vertices in set <b>u</b> are assigned even levels, starting from level 0.
   - Vertices in set <b>v</b> are assigned odd levels.
   - If an unmatched vertex in set <b>v</b> is reached, the BFS can terminate early as an augmenting path is found.
   - If no unmatched vertex in set <b>v</b> is reached, then there are no augmenting paths, and the algorithm terminates.
2. Augmenting Path Search (DFS):
   - Perform a depth-first search (DFS) to find augmenting paths in the level graph constructed in the previous step.
   - An augmenting path is a path that starts and ends at unmatched vertices and alternates between edges not in the matching and edges in the matching.
   - For each augmenting path found, augment the matching by reversing the matched and unmatched edges along the path.
3. Repeat:
   - Repeat the BFS to construct a new level graph and the DFS to find augmenting paths until no more augmenting paths can be found.
   - The algorithm terminates when the BFS cannot find any more augmenting paths, indicating that the maximum matching has been found.

### Uses
1. <b>Matching</b>: Eg - 1. Matching candidates to job openings. 2. Assigning students to schools based on preferences and availability.
2. <b>Data Clustering</b>: Eg - Use bipartite matching to pair data points or cluster centers in a way that minimizes the overall distance or dissimilarity.
3. <b>Resource Allocation</b>: Eg - Assigning delivery vehicles to routes based on capacity and demand.
4. <b>Scheduling</b>: Eg - Creating tournament schedules to avoid conflicts and maximize the number of matches.

https://www.youtube.com/watch?v=n7r4Dp6cVg8</br>
https://www.youtube.com/watch?v=GhjwOiJ4SqU