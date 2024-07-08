from collections import deque, defaultdict

def kahns_algorithm(num_nodes, adj_list):
    # Step 1: Compute in-degrees of all nodes
    in_degree = [0] * num_nodes

    for node in range(num_nodes):
        for neighbor in adj_list[node]:
            in_degree[neighbor] += 1

    # Step 2: Collect all nodes with in-degree of 0
    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    topological_order = []

    while queue:
        # Step 3: Remove a node from the queue and add it to the topological order
        node = queue.popleft()
        topological_order.append(node)

        # Step 4: Decrease in-degree of all its neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topological order contains all nodes, return it. Otherwise, there's a cycle.
    if len(topological_order) == num_nodes:
        return topological_order
    else:
        return "The graph contains a cycle."

# Example usage
num_nodes = 6
adj_list = {
    0: [1, 3],
    1: [],
    2: [0, 4],
    3: [1],
    4: [3, 5],
    5: [1]
}

print("Topological Sort of the given graph is:", kahns_algorithm(num_nodes, adj_list))