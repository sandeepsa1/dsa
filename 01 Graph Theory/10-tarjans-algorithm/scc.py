def tarjans_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = {}
    sccs = []

    # Helper function for the DFS
    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        # Consider successors of v
        for w in graph[v]:
            if w not in indices:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                # Successor w is in stack S and hence in the current SCC
                lowlink[v] = min(lowlink[v], indices[w])

        # If v is a root node, pop the stack and generate an SCC
        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    # Start the DFS from each node
    for v in graph:
        if v not in indices:
            strongconnect(v)

    return sccs

graph = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [4],
    4: [5, 7],
    5: [3, 6],
    6: [4],
    7: []
}

print("Strongly Connected Components of the given graph:")
result = tarjans_scc(graph)
print(result)