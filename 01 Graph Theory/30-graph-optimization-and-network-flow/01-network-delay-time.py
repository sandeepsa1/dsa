import heapq
from collections import defaultdict

def networkDelayTime(times, N, K):
    # Step 1: Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Step 2: Min-Heap to store (time, node), starting with the source node K
    min_heap = [(0, K)]  # (current_time, current_node)
    shortest_time = {}
    
    # Step 3: Dijkstra's Algorithm
    while min_heap:
        time, node = heapq.heappop(min_heap)
        if node in shortest_time:
            continue
        shortest_time[node] = time
        
        # Explore neighbors
        for neighbor, travel_time in graph[node]:
            if neighbor not in shortest_time:
                heapq.heappush(min_heap, (time + travel_time, neighbor))
    
    # Step 4: Check if all nodes are reached
    if len(shortest_time) == N:
        return max(shortest_time.values())
    return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
print(networkDelayTime(times, N, K))  # 2