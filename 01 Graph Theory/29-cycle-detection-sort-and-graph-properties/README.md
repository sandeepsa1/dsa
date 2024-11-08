## Cycle Detection, Topological Sorting, and Graph Properties
Algorithms on Cycle Detection, Topological Sorting, and Graph Properties.

Samples included are;
1. <b>Graph Coloring</b>: Assign colors to nodes such that no two adjacent nodes have the same color using a greedy approach.
2. <b>DFS-Based Cycle Detection</b>: Detect cycles in a directed graph using DFS.
3. <b>Union-Find Based Cycle Detection</b>: Detect cycles in an undirected graph using union-find data structure.
4. <b>Find the Town Judge</b>: In a town of n people, there is exactly one person who is trusted by everyone else but trusts no one. Find the town judge.
5. <b>Minimum Height Trees</b>: Given a tree of n nodes labeled from 0 to n-1, find all possible root nodes of a minimum height tree.
6. <b>Number of Connected Components in an Undirected Graph</b>: Given an undirected graph with n nodes and a list of edges, find the number of connected components.
7. <b>Course Schedule</b>: There are numCourses courses you have to take, numbered from 0 to numCourses-1. Some courses have prerequisites. Determine if it is possible to finish all courses.



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

### 3. Union-Find Based Cycle Detection
To detect cycles in an undirected graph using the Union-Find (Disjoint Set) data structure, follow below steps.

#### Steps
1. Union-Find Structure:
    - Create a union-find structure to keep track of connected components. Each node will point to its parent, and we'll use a rank to optimize the union operations.
2. Processing Edges:
    - For each edge in the graph, check if the two nodes are in the same connected component (i.e., they have the same root). If they are, it means adding this edge would create a cycle. If they are not, we perform a union operation to connect the components.
3. Cycle Detection:
    - If we find an edge connecting two nodes that are already in the same connected component, we have detected a cycle.

### 4. Find the Town Judge
To identify the town judge, find a person who is trusted by everyone else but does not trust anyone.

#### Steps
1. Initialize an array trust_count to keep track of each person’s trust status.
2. If person a trusts person b, then:
    - Decrease trust_count[a] by 1 (since a trusts someone else).
    - Increase trust_count[b] by 1 (since b is trusted by a).
3. After processing all trust relationships, the town judge should be the person with trust_count[i] == n - 1, meaning they’re trusted by everyone else but trust no one themselves.

### 5. Minimum Height Trees
To find all possible root nodes of a minimum height tree (MHT) in a given tree with n nodes labeled from 0 to n−1, use a "topological trim" approach. This method progressively removes leaves (nodes with only one connection) from the graph until only one or two nodes remain. These nodes are the centers of the tree, which yield the minimum height when used as roots.

#### Steps
1. Edge Case: If n=1, the only node is the root of the minimum height tree.
2. Initialize the Graph: Use an adjacency list to represent the tree, and record the degree (number of connections) of each node.
3. Identify Initial Leaves: Collect all nodes with only one edge (these are the initial leaves).
4. Topological Trimming:
    - Iteratively remove the current leaves, reducing the degree of their neighboring nodes.
    - Add any neighbors that become leaves (degree of 1) to the new leaves list.
    - Repeat until only one or two nodes remain, which are the possible roots for minimum height trees.

### 6. Number of Connected Components in an Undirected Graph
To find the number of connected components in an undirected graph, use Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse the graph. Each time a new traversal begins from an unvisited node, it indicates a new connected component.

#### Steps
1. Build an Adjacency List: Represent the graph using an adjacency list for efficient traversal.
2. Initialize Visited Set: Keep track of visited nodes to avoid counting the same component multiple times.
3. Traverse the Graph:
    - For each unvisited node, start a DFS (or BFS). This will visit all nodes in that component.
    - Increment the count of connected components each time you start a traversal from an unvisited node.

### 7. Course Schedule
To determine if it's possible to finish all courses given their prerequisites, this problem can be thought of as checking for cycles in a directed graph. Each course is a node, and each prerequisite is a directed edge from one course to another. If there's a cycle in the graph, it's impossible to complete all courses; otherwise, it's feasible.

#### Steps
1. Graph Representation: Represent the courses and their prerequisites as a directed graph using an adjacency list.
2. Cycle Detection with Topological Sort:
    - Use Kahn’s Algorithm (BFS approach) to perform topological sorting by counting in-degrees of each node.
    - Alternatively, use DFS with a recursion stack to detect cycles directly.
3. Topological Sort via BFS:
    - Initialize an in-degree count for each course.
    - Start from courses with an in-degree of 0 (those without prerequisites).
    - Reduce the in-degree of neighboring nodes and add them to the queue when their in-degree becomes 0.
    - If all nodes are processed (i.e., all courses can be taken in order), return True; otherwise, return False.