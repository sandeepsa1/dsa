from collections import defaultdict

def findBridges(n, connections):
    def dfs(node, parent, disc, low, adj, bridges):
        nonlocal time
        disc[node] = low[node] = time
        time += 1
        
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            
            if disc[neighbor] == -1:
                dfs(neighbor, node, disc, low, adj, bridges)
                
                low[node] = min(low[node], low[neighbor])
                
                if low[neighbor] > disc[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], disc[neighbor])
    
    # Step 1: Build the graph
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    
    # Step 2: Initialize discovery and low-link values
    disc = [-1] * n
    low = [-1] * n
    bridges = []
    time = 0  # Global timer
    
    # Step 3: Run DFS from each unvisited node
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1, disc, low, adj, bridges)
    
    return bridges


#  0 --- 1 --- 3 --- 4
#   \   /
#     2
n = 5
connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
print(findBridges(n, connections)) # [[3, 4], [1, 3]]