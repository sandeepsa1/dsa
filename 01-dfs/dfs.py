import networkx as nx
import matplotlib.pyplot as plt
import time

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            time.sleep(1)
            children = graph.get(current_node, [])
            for child in children[::-1]:
                stack.append(child)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

print("DFS traversal:")
dfs(tree, 'A')