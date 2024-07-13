## Depth First Search (DFS)
1. dfs.py
   - Basic Depth First Search algorithm
2. dfs_plotted.py
   - Depth First Search algorithm plotted using matplotlib
3. dfs_path_finding.py
   - To find path
4. dfs_spanning_tree.py
   - To find spanning tree
5. dfs_topological_sort.py
   - Topological sorting of nodes


### Uses
1. Graph Traversal:
   - DFS is primarily used for traversing or searching graphs. It starts at a selected node (the "root" or starting node) and explores as far as possible along each branch before backtracking. This traversal technique is useful for various graph-related problems, such as finding connected components, detecting cycles, and traversing paths.
2. Topological Sorting:
   - DFS can be used to perform topological sorting of directed acyclic graphs (DAGs). Topological sorting arranges the nodes of a graph in a linear ordering such that for every directed edge from node u to node v, u comes before v in the ordering. This ordering is useful for scheduling tasks or resolving dependencies in various applications.
3. Cycle Detection:
   - DFS can detect cycles in graphs by keeping track of visited nodes and exploring adjacent nodes recursively. If DFS encounters a visited node during traversal, it indicates the presence of a cycle in the graph. Cycle detection is essential in various applications, such as detecting deadlocks in resource allocation systems or identifying circular dependencies in software modules.
4. Path Finding:
   - DFS can find paths between two nodes in a graph. By recursively exploring adjacent nodes, DFS can identify paths from the starting node to the target node. This functionality is useful in applications such as route planning, maze solving, and network routing algorithms.
5. Maze Generation and Solving:
   - DFS can be used to generate and solve mazes. In maze generation, DFS creates a maze by recursively carving passages between adjacent cells until all cells are visited. In maze solving, DFS traverses the maze to find a path from the starting point to the goal.
6. Spanning Trees:
   - DFS can be used to find spanning trees of graphs. A spanning tree of a graph is a subset of edges that forms a tree connecting all the vertices without forming cycles. DFS explores the graph to construct a spanning tree by selecting edges that do not form cycles.
7. Connected Components:
   - DFS can identify connected components in an undirected graph. A connected component is a subgraph in which any two vertices are connected by paths. By performing DFS from each unvisited vertex, we can partition the graph into its connected components.
8. Articulation Points and Bridges:
   - DFS can identify articulation points (or cut vertices) and bridges (or cut edges) in a graph. Articulation points are vertices whose removal increases the number of connected components in the graph, while bridges are edges whose removal disconnects the graph. These concepts are crucial in network design and fault tolerance analysis