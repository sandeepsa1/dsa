class Node:
    def __init__(self, val: int, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]
        
        clone = Node(node.val)
        visited[node] = clone
        
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone

    return dfs(node)

def print_graph(node, visited=None):
    if visited is None:
        visited = set()
    
    if node in visited:
        return
    visited.add(node)
    
    print(f'Node {node.val}: {[n.val for n in node.neighbors]}')
    
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

cloned_graph = cloneGraph(node1)

print("Original graph:")
print_graph(node1)

print("\nCloned graph:")
print_graph(cloned_graph)