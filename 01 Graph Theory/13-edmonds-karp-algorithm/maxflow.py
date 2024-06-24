from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0

    def bfs(self, s, t, parent):
        visited = set()
        queue = deque([s])
        visited.add(s)
        parent[s] = -1

        while queue:
            u = queue.popleft()

            for v in self.graph[u]:
                if v not in visited and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == t:
                        return True

        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

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

    print("The maximum possible flow is %d" % g.edmonds_karp(source, sink))