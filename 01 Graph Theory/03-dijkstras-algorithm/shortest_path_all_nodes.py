import heapq

def dijkstra(graph, start):
    # 1. Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 2. Create a priority queue
    pqueue = [(0, start)] # (distance, node)
    
    while(pqueue): # 3. While there are still unvisited nodes
        node_dist, curr_node = heapq.heappop(pqueue)
        
        # Skip this node if we've already found a shorter path
        if node_dist > distances[curr_node]:
            continue
        
        # Update distances to child nodes
        children = graph[curr_node].items() # For dictionary
        for (child, weight) in children:
            if((node_dist + weight) < distances[child]):
                distances[child] = node_dist + weight
                heapq.heappush(pqueue, (distances[child], child))
    
    return distances

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'E': 3},
    'D': {'F': 1},
    'E': {'D': 2, 'F': 5},
    'F': {}
}
source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from node", source_node, ":", shortest_distances)
print("Total distance:", sum([value for value in shortest_distances.values()]))
