import heapq

def dijkstra(graph, source):
    # 1. Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # 2. Create a priority queue
    priority_queue = [(0, source)] # (distance, node)
    
    while priority_queue: # 3. While there are still unvisited nodes
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip this node if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Update distances to neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2}
}
source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from node", source_node, ":", shortest_distances)
print("Total distance:", sum([value for value in shortest_distances.values()]))