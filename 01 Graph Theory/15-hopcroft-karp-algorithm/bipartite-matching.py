from collections import deque, defaultdict

def bfs(graph, pair_u, pair_v, dist, U, V):
    queue = deque()
    for u in U:
        if pair_u[u] == None:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('Inf')
    dist[None] = float('Inf')
    
    while queue:
        u = queue.popleft()
        if dist[u] < dist[None]:
            for v in graph[u]:
                if dist[pair_v[v]] == float('Inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[None] != float('Inf')

def dfs(graph, pair_u, pair_v, dist, u):
    if u is not None:
        for v in graph[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(graph, pair_u, pair_v, dist, pair_v[v]):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = float('Inf')
        return False
    return True

def hopcroft_karp(graph, U, V):
    pair_u = {u: None for u in U}
    pair_v = {v: None for v in V}
    dist = {}
    
    matching = 0
    
    while bfs(graph, pair_u, pair_v, dist, U, V):
        for u in U:
            if pair_u[u] == None:
                if dfs(graph, pair_u, pair_v, dist, u):
                    matching += 1
                    
    return matching, pair_u, pair_v


graph = {
    1: [4, 5],
    2: [5, 6],
    3: [6]
}

U = {1, 2, 3}
V = {4, 5, 6}

matching, pair_u, pair_v = hopcroft_karp(graph, U, V)
print(f"Maximum Matching: {matching}")
print(f"pair_u: {pair_u}")
print(f"pair_v: {pair_v}")