from collections import defaultdict

def countComponents(n, edges):
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Initialize visited set and component count
    visited = set()
    component_count = 0

    # Step 3: Define DFS function to traverse a component
    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # Step 4: Traverse each node, starting DFS from unvisited nodes
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            component_count += 1

    return component_count


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n, edges))  # 2