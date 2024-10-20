## Cycle Detection, Topological Sorting, and Graph Properties
Algorithms on Cycle Detection, Topological Sorting, and Graph Properties.

Samples included are;
1. <b>Graph Coloring</b>: Assign colors to nodes such that no two adjacent nodes have the same color using a greedy approach.
2. <b>DFS-Based Cycle Detection</b>: Detect cycles in a directed graph using DFS.


### 1. Graph Coloring
The Graph Coloring Problem involves assigning colors to nodes in a graph such that no two adjacent nodes share the same color. One common approach to this problem is the Greedy Coloring Algorithm.

#### Steps
1. Start by initializing all nodes as uncolored.
2. Assign the first node a color (let's say color 1).
3. For each subsequent node:
    - Check the colors of its adjacent nodes.
    - Assign the smallest color (starting from 1) that has not been assigned to its adjacent nodes.
4. Repeat this process until all nodes are colored.

### 2. DFS-Based Cycle Detection
To detect cycles in a directed graph using Depth-First Search (DFS), perform a traversal of the graph and track the recursion stack to identify back edges that indicate cycles. A back edge is an edge that points from a node back to one of its ancestors in the DFS tree, which is a hallmark of a cycle.

#### Steps
1. Start DFS from each unvisited node.
2. For each node, mark it as visited and add it to the recursion stack.
3. Recursively visit all adjacent nodes.
4. If you encounter a node that is already in the recursion stack, a cycle exists.
5. After processing the current node, remove it from the recursion stack.