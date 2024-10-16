## Cycle Detection, Topological Sorting, and Graph Properties
Algorithms on Cycle Detection, Topological Sorting, and Graph Properties.

Samples included are;
1. <b>Graph Coloring</b>: Assign colors to nodes such that no two adjacent nodes have the same color using a greedy approach.


### 1. Graph Coloring
The Graph Coloring Problem involves assigning colors to nodes in a graph such that no two adjacent nodes share the same color. One common approach to this problem is the Greedy Coloring Algorithm.

#### Steps
1. Start by initializing all nodes as uncolored.
2. Assign the first node a color (let's say color 1).
3. For each subsequent node:
    - Check the colors of its adjacent nodes.
    - Assign the smallest color (starting from 1) that has not been assigned to its adjacent nodes.
4. Repeat this process until all nodes are colored.