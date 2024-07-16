## Second shortest path in a weighted graph
Finding the second shortest path in a weighted graph involves finding the shortest paths and then adjusting the graph to search for an alternative path.</br>

1. Time complexity: <b>𝑂(E log V)</b>
2. Space complexity: <b>𝑂(V + E)</b></br>


### Steps
1. Find all the shortest path between the provided vertices using Dijkstra's algorithm.
2. Find the second shortest path by temporarily removing edges of the shortest path and using Dijkstra's again.
3. The minimum of the distances found in step 2 is the second shortest path distance. If no such path exists, return None

### Uses
The second shortest path algorithm is used in network routing to provide alternative routes. It is also useful in logistics and transportation planning to identify backup routes.