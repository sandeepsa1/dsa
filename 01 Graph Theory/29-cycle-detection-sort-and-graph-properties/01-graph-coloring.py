def greedy_coloring(graph):
    num_nodes = len(graph)
    result = [-1] * num_nodes
    
    # Assign the first color to the first node
    result[0] = 0
    
    available_colors = [False] * num_nodes
    
    # Assign colors to the rest of the nodes
    for node in range(1, num_nodes):
        for neighbor in graph[node]:
            if result[neighbor] != -1:
                available_colors[result[neighbor]] = True
        
        # Find the first available color
        color = 0
        while color < num_nodes and available_colors[color]:
            color += 1
        
        # Assign the found color to the current node
        result[node] = color
        
        # Reset the available_colors array for the next iteration
        for neighbor in graph[node]:
            if result[neighbor] != -1:
                available_colors[result[neighbor]] = False
    
    for node in range(num_nodes):
        print(f"Node {node} is colored with color {result[node]}")
    
    return result


graph = [
    [1, 2],
    [0, 2],
    [0, 1]
]

greedy_coloring(graph)