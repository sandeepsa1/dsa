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