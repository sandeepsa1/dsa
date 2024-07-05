from collections import deque, defaultdict

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# BFS to build the level graph
def bfs(U, V, pair_u, pair_v, dist):
    queue = deque()
    for u in U:
        if pair_u[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[0] = float('inf')
    while queue:
        u = queue.popleft()
        if dist[u] < dist[0]:
            for v in adj[u]:
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[0] != float('inf')

# DFS to find augmenting paths
def dfs(u, pair_u, pair_v, dist):
    if u != 0:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(pair_v[v], pair_u, pair_v, dist):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = float('inf')
        return False
    return True

# Hopcroft-Karp algorithm
def hopcroft_karp(U, V):
    pair_u = {u: 0 for u in U}
    pair_v = {v: 0 for v in V}
    dist = {}
    matching = 0
    while bfs(U, V, pair_u, pair_v, dist):
        for u in U:
            if pair_u[u] == 0:
                if dfs(u, pair_u, pair_v, dist):
                    matching += 1
    return matching, pair_u

if __name__ == "__main__":
    U = {1, 2, 3}
    V = {4, 5, 6}
    adj = defaultdict(list)
    
    add_edge(adj, 1, 4)
    add_edge(adj, 1, 5)
    add_edge(adj, 2, 5)
    add_edge(adj, 2, 6)
    add_edge(adj, 3, 6)
    
    matching, pairs = hopcroft_karp(U, V)
    print(f"Maximum Matching: {matching}")
    print(f"Matching Pairs: {pairs}")