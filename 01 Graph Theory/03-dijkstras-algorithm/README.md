1. shortest_path.py
Dijkstra's algorithm code to find shortest path

Dijkstra's algorithm
    Dijkstra's algorithm is a graph search algorithm used to find the shortest path between nodes in a weighted graph.

Uses
    It's commonly used in many applications, including computer networking (routing protocols), GPS systems, and various optimization problems.

How it works
    The algorithm works by iteratively exploring the nodes of the graph, starting from a source node and updating the shortest distance to each node as it progresses. At each step, it selects the node with the shortest distance from the source that has not yet been visited. It then updates the distances to its neighbors based on the edge weights and the current shortest distances.

    Dijkstra's algorithm can handle both directed and undirected graphs, but it requires non-negative edge weights. If the graph contains negative edge weights, other algorithms like Bellman-Ford may be more appropriate.

Dijkstra's algorithm
    1. Initialize distances: Assign a tentative distance of zero to the source node and infinity to all other nodes.
    2. Create a priority queue (or use a min-heap) to keep track of nodes with the smallest tentative distance.
    3. While there are still unvisited nodes:
        a. Select the unvisited node with the smallest tentative distance.
        b. For each neighbor of the current node:
            i. Calculate the distance from the source to the neighbor through the current node.
            ii. If this distance is less than the neighbor's current tentative distance, update the neighbor's distance.
    4. Mark the current node as visited.
    5. Repeat until all nodes have been visited.
The algorithm terminates when all nodes have been visited, and the shortest distance to each 