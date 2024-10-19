def isCyclicUtil(node, visited, recStack, graph):
    visited[node] = True
    recStack[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if isCyclicUtil(neighbor, visited, recStack, graph):
                return True
        elif recStack[neighbor]:
            return True
    
    recStack[node] = False
    return False

def isCyclic(graph, numNodes):
    visited = [False] * numNodes
    recStack = [False] * numNodes
    
    for node in range(numNodes):
        if not visited[node]:
            if isCyclicUtil(node, visited, recStack, graph):
                return True
    return False


graph = [
    [1],
    [2],
    [0],
    [4],
    []
]

numNodes = len(graph)

if isCyclic(graph, numNodes):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")