from collections import defaultdict, deque

def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]
    
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Step 2: Collect initial leaves (nodes with degree 1)
    leaves = deque([i for i in range(n) if degree[i] == 1])

    # Step 3: Trim the leaves level by level
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count

        for _ in range(leaves_count):
            leaf = leaves.popleft()
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)

    # The remaining nodes are the root(s) of the minimum height tree(s)
    return list(leaves)


n = 6
edges = [[0, 3], [3, 1], [3, 2], [1, 4], [2, 5]]
print(findMinHeightTrees(n, edges)) # [3]