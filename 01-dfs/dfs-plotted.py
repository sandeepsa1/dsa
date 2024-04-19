import networkx as nx
import matplotlib.pyplot as plt
import time


G = nx.Graph()

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G'), ('D', 'H'), ('D', 'I')]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Binary tree-like structure
pos = {'A': (0, 3), 'B': (-1, 2), 'C': (1, 2), 'D': (-2, 1), 'E': (0, 1), 'F': (2, 1), 'G': (0, 0), 'H': (-3, 0), 'I': (-1, 0)}

#plt.figure(figsize=(8, 6))
#nx.draw(G, pos, with_labels=True, node_size=1500, node_color='red', font_size=12, font_weight='bold', edge_color='black')

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    
    plt.figure(figsize=(7, 5))
    plt.title('DFS Traversal')
    
    while stack:
        node = stack.pop()
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='yellow')
        nx.draw_networkx_nodes(G, pos, nodelist=neighbors, node_color='grey')
        nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color='blue')
        nx.draw_networkx_edges(G, pos)
        plt.pause(2)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                
        plt.clf()  # Clear the plot to update it with the next traversal step
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='red', font_size=12, font_weight='bold', edge_color='black')
        plt.title('DFS Traversal')

dfs(G, 'A')
