## Kahn's Algorithm
Kahn's algorithm is used for topological sorting of a directed acyclic graph (DAG). It works by repeatedly removing nodes with no incoming edges and appending them to the topological order.</br>

1. Time complexity: 𝑂(V + E)
2. Space complexity: 𝑂(V + E)


### Uses
1. Task Scheduling:
   1. <b>Project Management</b>: Determines the order of tasks based on dependencies.
   1. <b>Job Scheduling</b>: Schedules jobs in computer systems without violating dependencies.
2. Course Prerequisites:
   1. <b>Curriculum Planning</b>: Orders courses to be taken based on prerequisite relationships.
3. Build Systems:
   1. <b>Compilation Order</b>: Determines the order of file compilation based on dependencies.
4. Data Serialization:
   1. <b>Object Serialization</b>: Saves dependent objects in the correct order.
5. Circuit Design:
   1. <b>Logic Gates Evaluation</b>: Determines the order of evaluation in digital circuits.

### How it works
1. Compute the in-degree (number of incoming edges) for each node.
2. Collect all nodes with an in-degree of 0 in a queue.
3. While the queue is not empty:
   - Remove a node from the queue.
   - Append it to the topological order.
   - Decrease the in-degree of all its neighbors by 1.
   - If any neighbor's in-degree becomes 0, add it to the queue.
4. If the topological order contains all the nodes, the graph is a DAG. Otherwise, it contains a cycle.

### Comparison with DFS
1. Approach:
   - <b>Kahn's</b>: Kahn's algorithm uses in-degree (number of incoming edges) to identify nodes with no incoming edges, which are then processed in a queue.
   - <b>DFS</b>: The DFS-based algorithm uses a stack to store the nodes in the order of their completion times, producing a reverse post-order of the DFS.
2. When to Use:
   - <b>Kahn's</b>: Suitable for situations where detecting cycles is also important, as it naturally identifies if the graph contains a cycle.
   - <b>DFS</b>: Naturally integrates with DFS, which can be useful for other graph algorithms. Efficient in terms of space, as it doesn't need an additional in-degree array.
3. Disadvantages:
   - <b>Kahn's</b>: Requires additional space for the in-degree array. The result may not be unique; different valid orders are possible based on the initial queue state.
   - <b>DFS</b>: More complex to implement and understand, especially for beginners. The result may not be unique; different valid orders are possible based on the initial DFS path.
4. Complexity: Both are having same time complexity and space complexity is slightly better for DFS.

https://www.youtube.com/watch?v=cIBFEhD77b4