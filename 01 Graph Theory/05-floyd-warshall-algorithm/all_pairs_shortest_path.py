import sys

 # Refer README.md to understand the steps.
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    #print(dist)
    
    # Populate n * n matrix with values
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    #print(dist)

    # Calculate shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Graph contains negative-weight cycle")
            return None

    return dist

graph = [
    [0, 3, 0, 0, 5],
    [0, 0, 4, 0, 0],
    [0, 2, 0, -2, 0],
    [0, 0, 4, 0, 2],
    [0, 5, 0, 1, 0]
]

shortest_paths = floyd_warshall(graph)
if shortest_paths:
    print("Shortest paths between all pairs of vertices:")
    for row in shortest_paths:
        print(row)