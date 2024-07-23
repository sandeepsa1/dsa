def find_longest_path(graph, start, end):
    def dfs(node, end, path, memo):
        if node == end:
            return path
        if node in memo:
            return memo[node]
        
        max_path = []
        for neighbor in graph.get(node, []):
            new_path = dfs(neighbor, end, path + [neighbor], memo)
            if len(new_path) > len(max_path):
                max_path = new_path
        
        memo[node] = max_path
        return max_path

    # Initialize memoization dictionary
    memo = {}
    # Start DFS from the start node
    longest_path = dfs(start, end, [start], memo)
    
    return longest_path

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G', 'K'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': ['J'],
    'J': ['K']
}

start = 'A'
end = 'K'

# Find the longest path
longest_path = find_longest_path(graph, start, end)
print("Longest path from {} to {}:".format(start, end), longest_path)