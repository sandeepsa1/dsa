## Minimum Cost Maximum Flow Algorithm
This implementation of the Minimum Cost Maximum Flow algorithm uses a basic implementation of the Successive Shortest Path Algorithm (SSPA) combined with Bellman-Ford to find shortest paths.</br></br>
In a Flow network we may be able to achieve maximum flow using different combination of paths. Idea is to achieve this maximum flow value for the path combinations that provide the minimum cost.</br>

For example below 2 combinations produce the max flow of 19 for the sample input (Refer image also).</br>
But the first combination of paths achieve this with the minimum cost of 149.</br>
&emsp;S -> A -> D -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;8</br>
&emsp;S -> C -> D -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2</br>
&emsp;S -> A -> B -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;2</br>
&emsp;S -> C -> D -> A -> B -> T&emsp;&nbsp;2</br>
&emsp;S -> C -> D -> B -> T&emsp;&emsp;&emsp;&emsp;5</br>
&emsp;S -> A -> B -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4</br>
&emsp;S -> A -> D -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;6</br>
&emsp;S -> C -> D -> T&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4</br>
&emsp;S -> C -> D -> B -> T&emsp;&emsp;&emsp;&emsp;5</br></br>

1. Time complexity: <b>𝑂(F . V . E)</b> where F is the maximum flow.
2. Space complexity: <b>𝑂(V . E)</b></br>


### How it works
1. Graph Construction:
   1. Create a graph structure to store capacities and costs.
   1. For each edge, store the forward capacity and cost, and initialize the reverse edge with zero capacity and the negative of the original cost.
2. Bellman-Ford Algorithm:
   1. Used to find the shortest path from the source to all other nodes.
   1. Updates distances and parent pointers for the shortest path.
3. Flow Augmentation:
   1. Adjust the flow along the shortest path found by Bellman-Ford.
   1. Update the capacities in the residual graph.
4. Main Loop::
   1. Repeatedly find shortest paths and augment flow until no more paths from the source to the sink.

### Uses
The Minimum Cost Maximum Flow algorithm is used in network optimization problems where both flow quantity and cost need to be minimized, such as in transportation logistics, supply chain management, and telecommunication networks. It helps in optimizing resources and minimizing expenses while satisfying flow constraints and capacity limits.