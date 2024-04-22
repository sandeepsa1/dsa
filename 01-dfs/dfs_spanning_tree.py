import matplotlib.pyplot as plt
import networkx as nx

def dfs(graph, node, visited, spanning_tree):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            spanning_tree.add_edge(node, neighbor)
            dfs(graph, neighbor, visited, spanning_tree)


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Initialize visited set and spanning tree
visited = set()
spanning_tree = nx.Graph()

# Start DFS from an arbitrary node
start_node = list(G.nodes())[0]
dfs(G, start_node, visited, spanning_tree)

# Display the spanning tree
pos = nx.spring_layout(spanning_tree)  # Define node positions
nx.draw(spanning_tree, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='black')
plt.title('Spanning Tree')
plt.show()