## A* algorithm
The A* algorithm works by combining features of Dijkstra's algorithm and Greedy Best-First-Search. It uses a heuristic function to guide the search for the shortest path. The "A*" (A-star) symbol in the A* search algorithm represents a star and is used to denote an improvement or enhancement over previous algorithms.</br>
A heuristic is a technique that guides problem-solving and decision-making processes. In the context of algorithms like A*, a heuristic provides an estimate of the cost or distance from a given state to the goal state. This estimate helps guide the search towards the goal in a more efficient manner.</br>
As an example, consider a graph of [m,n] dimension and each of the node in the graph is equally spaced. If start is [0, 0] and goal is to reach [m,n] node, Dijkstra's will traverse through each node to find the shortest path, making it less efficient. If we can include a heuristic function that calculates euclidean the disance to the goal on each iteration, we can do a better selection of next nodes to reach the goals faster and that is the idea of A* algorithm.</br>
https://www.youtube.com/watch?v=6TsL96NAZCo

1. Time complexity:
   1. Worst case: 𝑂(b<sup>d</sup>)
   2. Best case: 𝑂(d)
2. Space complexity:
   1. Worst case: 𝑂(b<sup>d</sup>)</br>

b is the the average number of successors per state. d is the depth of the shortest path.


### Uses
1. Game Development:
   1. Pathfinding for NPCs: A* is extensively used in games to calculate the shortest and most efficient path for non-player characters (NPCs) to navigate through the game world.
   2. Real-time Strategy Games: Helps in determining the movement of units and characters, avoiding obstacles while reaching the target efficiently.
2. Robotics:
   1. Autonomous Navigation: Robots use A* for path planning to move from one point to another while avoiding obstacles.
   2. Obstacle Avoidance: Ensures that the robot can navigate through environments with dynamic obstacles.
3. Navigation Systems:
   1. GPS and Mapping: Used in GPS systems to find the shortest path between two locations considering various road constraints.
   2. Route Optimization: Helps in optimizing routes for delivery services, ride-sharing applications, and logistics.
4. Artificial Intelligence:
   1. AI in Virtual Environments: Used in virtual reality and simulations for efficient movement and interaction within the environment.
   2. Search Problems: Solves various AI problems that require finding the shortest path, such as puzzle solving and decision making.
5. Geographical Information Systems (GIS): Terrain Navigation. Urban Planning
6. Network Routing: Optimal Routing, Load Balancing
7. Puzzle Solving: Puzzles like 8-Puzzle and 15-Puzzle, Rubik’s Cube

### How it works
1. Initialize:
   1. Create two lists: open list (nodes to be evaluated) and closed list (nodes already evaluated). Start by adding the initial node to the open list.
   2. Initialize two maps: 'g' for the cost from the start node to the current node and 'f' for the estimated cost from the start node to the goal through the current node.
2. Iterate:
   1. While the open list is not empty:
      1. Select the node with the lowest 'f' value from the open list.
      2. If this node is the goal, reconstruct and return the path.
      3. Move the current node to the closed list.
3. Evaluate Neighbors:
   1. For each neighbor of the current node:
      1. If the neighbor is in the closed list, ignore it.
      2. Calculate tentative 'g' value (cost to move from the start node to the neighbor through the current node).
      3. If the neighbor is not in the open list or the tentative 'g' value is lower than the previously recorded 'g' value:
         1. Update the 'g' and 'f' values for the neighbor.
         2. Set the current node as the neighbor's parent.
         3. If the neighbor is not in the open set, add it.

### Properties of A*
1. Optimality: A* is guaranteed to find the shortest path if the heuristic function h(n) is admissible (never overestimates the true cost) and consistent (satisfies the triangle inequality).
2. Completeness: A* will always find a path if one exists, provided the graph is finite and the heuristic is admissible.
3. Efficiency: A* is more efficient than uninformed search algorithms due to its heuristic guidance.

### Comparison with Dijkstra's Algorithm
1. A* is generally more efficient with good heuristic. Dijkstra's Algorithm is less efficient for large graphs.
2. A* used for mainly navigation, games, robot motion planning. Dijkstra's is used for network routing, shortest paths from a single source to all nodes.
2. In summary, A* is preferred when a good heuristic is available and you need the shortest path to a specific goal. Dijkstra's algorithm is used when you need the shortest paths from a single source to all other nodes, or when no heuristic information is available.