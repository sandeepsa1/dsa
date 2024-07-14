## Second shortest path in an unweighted graph
Finding the second shortest path in an unweighted graph involves finding the shortest paths and then adjusting the graph to search for an alternative path.</br>

1. Time complexity: <b>𝑂(V. (V + E) )</b>
2. Space complexity: <b>𝑂(V<sup>2</sup>)</b></br>


### Steps
1. Find all the shortest paths between the provided vertices using BFS.
2. Find the second shortest path by temporarily removing edges of the shortest paths and using BFS again.
3. The minimum of the distances found in step 2 is the second shortest path distance. If no such path exists, return None

### Uses
Finding the second shortest path in a graph is crucial for applications in network routing, transportation, and logistics. It provides redundancy and failover options to ensure reliability and efficiency in communication networks, transportation systems, and emergency response planning. This approach also aids in load balancing, optimizing delivery routes, and enhancing fault tolerance in data centers and cloud computing.