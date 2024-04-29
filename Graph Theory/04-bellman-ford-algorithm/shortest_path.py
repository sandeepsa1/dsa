def bellman_ford(graph, source):
    # Step 1: Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(len(graph) - 1):
        updated = False  # Flag to track if any distance is updated
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    updated = True  # Set flag to True if distance is updated
        if not updated:
            break  # If no distance is updated, terminate early
    
    # Step 3: Check for negative-weight cycles
    if updated:  # If any distance is updated in the final iteration, there is a negative-weight cycle
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = float('-inf')

    return distances

# Sample graph represented as an adjacency list
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

# Source node
source = 'A'

# Find shortest distances from the source node
distances = bellman_ford(graph, source)

# Print the distances
print("Shortest distances from", source, "to all other nodes:")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")