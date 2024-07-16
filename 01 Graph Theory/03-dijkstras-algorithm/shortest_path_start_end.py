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

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('E', 3)],
    'D': [('F', 1)],
    'E': [('D', 2), ('F', 5)],
    'F': []
}
source_node = 'A'
end_node = 'F'
shortest_cost, shortest_path = dijkstra(graph, source_node, end_node)
print("Shortest Distance", shortest_cost)
print("Shortest Path:", shortest_path)
