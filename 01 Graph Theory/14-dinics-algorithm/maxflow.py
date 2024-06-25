from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.capacity = {}
        self.vertices = set()

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0
        self.vertices.update([u, v])

    def bfs(self, s, t, level):
        for vertex in self.vertices:
            level[vertex] = -1
        level[s] = 0

        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if level[v] < 0 and self.capacity[(u, v)] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level[t] >= 0

    def dfs(self, u, t, flow, level, start):
        if u == t:
            return flow

        while start[u] < len(self.graph[u]):
            v = self.graph[u][start[u]]
            if level[v] == level[u] + 1 and self.capacity[(u, v)] > 0:
                min_cap = min(flow, self.capacity[(u, v)])
                pushed_flow = self.dfs(v, t, min_cap, level, start)

                if pushed_flow > 0:
                    self.capacity[(u, v)] -= pushed_flow
                    self.capacity[(v, u)] += pushed_flow
                    return pushed_flow
            
            start[u] += 1

        return 0

    def dinic(self, source, sink):
        if source == sink:
            return 0

        max_flow = 0
        level = {}

        while self.bfs(source, sink, level):
            start = {vertex: 0 for vertex in self.vertices}
            while True:
                flow = self.dfs(source, sink, float('Inf'), level, start)
                if flow == 0:
                    break
                max_flow += flow

        return max_flow

if __name__ == "__main__":
    g = Graph()
    g.add_edge('S', 'A', 10)
    g.add_edge('S', 'C', 10)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('A', 'D', 8)
    g.add_edge('C', 'D', 9)
    g.add_edge('D', 'B', 6)
    g.add_edge('B', 'T', 10)
    g.add_edge('D', 'T', 10)

    source = 'S'
    sink = 'T'

    print("The maximum possible flow is %d" % g.dinic(source, sink))