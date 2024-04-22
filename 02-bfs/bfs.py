from collections import deque
import time

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            time.sleep(1)
            queue.extend(graph[node] - visited)

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

start_node = 'A'
print("BFS Traversal:")
bfs(graph, start_node)