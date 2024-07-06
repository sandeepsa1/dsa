from collections import defaultdict

def kosaraju(graph):
    def dfs_first_pass(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs_first_pass(neighbor)
        stack.append(v)
    
    def dfs_second_pass(v, component):
        visited[v] = True
        component.append(v)
        for neighbor in transposed_graph[v]:
            if not visited[neighbor]:
                dfs_second_pass(neighbor, component)
    
    # Step 1: DFS on original graph
    visited = {v: False for v in graph}
    stack = []
    for v in graph:
        if not visited[v]:
            dfs_first_pass(v)
    
    # Step 2: Transpose the graph
    transposed_graph = {v: [] for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            transposed_graph[neighbor].append(v)
    
    # Step 3: DFS on transposed graph
    visited = {v: False for v in graph}
    sccs = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_second_pass(v, component)
            sccs.append(component)
    
    return sccs

if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0] = [1]
    graph[1] = [2, 3]
    graph[2] = [0]
    graph[3] = [4]
    graph[4] = [5, 7]
    graph[5] = [3, 6]
    graph[6] = [4]
    graph[7] = []
    sccs = kosaraju(graph)
    print(f"Strongly Connected Components: {sccs}")