def find_longest_path(graph, start, end):
    def dfs(node, end, memo):
        if node == end:
            return (0, [end])
        if node in memo:
            return memo[node]
        
        max_length = float('-inf')
        max_path = []
        
        for neighbor, weight in graph[node].items():
            current_length, current_path = dfs(neighbor, end, memo)
            current_length += weight
            
            if current_length > max_length:
                max_length = current_length
                max_path = [node] + current_path
        
        memo[node] = (max_length, max_path)
        return memo[node]
    
    memo = {}
    
    # Start the DFS from the start node
    max_distance, longest_path = dfs(start, end, memo)
    
    return max_distance, longest_path

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'E': 3},
    'D': {'F': 1},
    'E': {'D': 2, 'F': 5},
    'F': {}
}
start = 'A'
end = 'F'

max_distance, longest_path = find_longest_path(graph, start, end)
print("Longest path from {} to {}:".format(start, end), longest_path)
print("Length of the longest path:", max_distance)