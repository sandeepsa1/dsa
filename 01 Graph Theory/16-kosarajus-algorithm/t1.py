def dfs_first_pass(v, visited):
    stack = []
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_first_pass(neighbor, visited)
    stack.append(v)
    return stack

def dfs_second_pass(v, component, transposed_graph, visited):
    visited[v] = True
    component.append(v)
    for neighbor in transposed_graph[v]:
        if not visited[neighbor]:
            dfs_second_pass(neighbor, component)
    return component

def transpose_graph(graph):
    transposed_graph = {v: [] for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            transposed_graph[neighbor].append(v)
    return transposed_graph

def kosaraju(graph):    
    # Step 1: First pass (DFS on original graph)
    visited = {v: False for v in graph}
    stack = []
    for v in graph:
        if not visited[v]:
            stack.append(dfs_first_pass(v, visited))
    
    # Step 2: Transpose the graph
    transposed_graph = transpose_graph(graph)
    
    # Step 3: Second pass (DFS on transposed graph)
    visited = {v: False for v in graph}
    sccs = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = dfs_second_pass(v, component, transposed_graph, visited)
            sccs.append(component)
    
    return sccs

# Sample usage
if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [5, 7],
        5: [6],
        6: [4],
        7: [3, 8],
        8: [9],
        9: [7]
    }
    sccs = kosaraju(graph)
    print(f"Strongly Connected Components: {sccs}")