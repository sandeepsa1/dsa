import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (cost, current_node, path)
    pq = [(0, start, [])]
    visited = set()
    
    while pq:
        (cost, current_node, path) = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        if current_node == end:
            return cost, path
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))
    
    return float('inf'), []

def second_shortest_path(graph, start, end):
    # Find the shortest path
    shortest_cost, shortest_path = dijkstra(graph, start, end)
    if not shortest_path:
        return None, None
    
    second_shortest_cost = float('inf')
    second_shortest_path = []
    
    # Try removing each edge in the shortest path and find the new shortest path
    for i in range(len(shortest_path) - 1):
        u, v = shortest_path[i], shortest_path[i + 1]
        
        # Remove edge (u, v)
        original_edges = graph[u]
        graph[u] = [(node, weight) for node, weight in graph[u] if node != v]
        
        new_cost, new_path = dijkstra(graph, start, end)
        
        if new_cost > shortest_cost and new_cost < second_shortest_cost:
            second_shortest_cost = new_cost
            second_shortest_path = new_path
        
        # Restore edge (u, v)
        graph[u] = original_edges
    
    return shortest_cost, shortest_path, second_shortest_cost, second_shortest_path

# Example usage

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('E', 3)],
    'D': [('F', 1)],
    'E': [('D', 2), ('F', 5)],
    'F': []
}

start_node = 'A'
end_node = 'F'
shortest_cost, shortest_path, second_path_cost, second_path = second_shortest_path(graph, start_node, end_node)

print("Shortest Path Cost:", shortest_cost)
print("Shortest Path:", shortest_path)
print("Second Shortest Path Cost:", second_path_cost)
print("Second Shortest Path:", second_path)