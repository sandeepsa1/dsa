import bellman_ford as b
import dijkstra as d

# Johnson's algorithm for finding shortest paths between all pairs of vertices
# in a weighted graph with negative edges also.

# Sample graph
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

def add_vertex_q(graph):
    graph['q'] = {}
    for vertex in graph:
        if vertex != 'q':
            graph['q'][vertex] = 0
    return graph

def reweight_graph(graph, h):
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v in graph[u]:
            reweighted_graph[u][v] = graph[u][v] + h[u] - h[v]
    return reweighted_graph

def johnson(graph):
    # Step 1: Add a new vertex 'q' and connect it to every other vertex with an edge of weight 0
    graph_with_q = add_vertex_q(graph.copy())
    
    # Step 2: Run Bellman-Ford algorithm from 'q'
    try:
        h = b.bellman_ford(graph_with_q, 'q')
    except ValueError as e:
        print(e)
        return
    
    # Step 3: Reweight the edges
    reweighted_graph = reweight_graph(graph, h)
    
    all_pairs_shortest_paths = {}
    
    for u in graph:
        # Step 4: Run Dijkstra's algorithm for each vertex
        shortest_paths_from_u = d.dijkstra(reweighted_graph, u)
        all_pairs_shortest_paths[u] = {}
        
        # Step 5: Adjust the weights to get the actual shortest path distances
        for v in shortest_paths_from_u:
            if v in h:
                all_pairs_shortest_paths[u][v] = shortest_paths_from_u[v] + h[v] - h[u]
    
    return all_pairs_shortest_paths

all_pairs_shortest_paths = johnson(graph)

# Print results
if all_pairs_shortest_paths:
    for u in all_pairs_shortest_paths:
        for v in all_pairs_shortest_paths[u]:
            distance = all_pairs_shortest_paths[u][v]
            if distance != float('inf'):
                print(f"Shortest path from {u} to {v} is {distance}")