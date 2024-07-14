from collections import deque, defaultdict

def bfs(graph, start, end): # Returns all shortest paths
    queue = deque([(start, [start])])
    visited = set()
    shortest_paths = []
    shortest_distance = float('inf')

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == end:
            if len(path) < shortest_distance:
                shortest_distance = len(path)
                shortest_paths = [path]
            elif len(path) == shortest_distance:
                shortest_paths.append(path)
            continue

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return shortest_paths, shortest_distance

def second_shortest_path(graph, start, end):
    shortest_paths, shortest_distance = bfs(graph, start, end)
    print(shortest_paths)

    second_shortest_distance = float('inf')
    second_shortest_path = None
    for path in shortest_paths:
        # Remove one edge at a time of the shortest path to find second shortest path
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            
            if v in graph[u]:
                graph[u].remove(v)
                new_paths, new_distance = bfs(graph, start, end)
                graph[u].append(v)

                if new_distance > shortest_distance and new_distance < second_shortest_distance:
                    second_shortest_distance = new_distance
                    if new_paths:
                        second_shortest_path = new_paths[0]

    return second_shortest_path, second_shortest_distance if second_shortest_distance < float('inf') else None


if __name__ == "__main__":
    graph = { # ['A', 'C', 'K'] is the shortest path
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G', 'K'],
        'D': ['H'],
        'E': [],
        'F': ['I'],
        'G': ['J'],
        'J': ['K']
    }
    start = 'A'
    end = 'K'

    second_path, second_distance = second_shortest_path(graph, start, end)
    if second_path is None:
        print("There is no second shortest path.")
    else:
        print("Second shortest path:", second_path)
        print("Second shortest path length:", second_distance)