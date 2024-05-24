from collections import defaultdict

class TarjanSCC:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.index = 0
        self.stack = []
        self.indexes = [-1] * self.V
        self.lowlinks = [-1] * self.V
        self.on_stack = [False] * self.V
        self.sccs = []

    def strongconnect(self, v):
        self.indexes[v] = self.index
        self.lowlinks[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for w in self.graph[v]:
            if self.indexes[w] == -1:
                self.strongconnect(w)
                self.lowlinks[v] = min(self.lowlinks[v], self.lowlinks[w])
            elif self.on_stack[w]:
                self.lowlinks[v] = min(self.lowlinks[v], self.indexes[w])

        if self.lowlinks[v] == self.indexes[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            self.sccs.append(scc)

    def get_sccs(self):
        for v in range(self.V):
            if self.indexes[v] == -1:
                self.strongconnect(v)
        return self.sccs

# Example usage
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

    tarjan = TarjanSCC(graph)
    sccs = tarjan.get_sccs()
    print("Strongly Connected Components:", sccs)