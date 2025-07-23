# 'A' is friends with 'B' and 'C'. Suggest friends for 'A'
from collections import deque, defaultdict

def suggest_friends(graph, user):
    visited = set()
    queue = deque()
    level = {}
    suggestions = defaultdict(int)

    queue.append((user, 0))
    visited.add(user)
    level[user] = 0

    while queue:
        current, depth = queue.popleft()
        if depth > 2:
            break
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                level[neighbor] = depth + 1
                queue.append((neighbor, depth + 1))
                if level[neighbor] == 2 and neighbor not in graph[user]:
                    # Count mutual connections
                    mutuals = set(graph[user]).intersection(set(graph[neighbor]))
                    suggestions[neighbor] = len(mutuals)

    return dict(sorted(suggestions.items(), key=lambda x: -x[1]))  # sort by most mutuals


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

suggested = suggest_friends(graph, 'A')
print("Friend Suggestions for A:", suggested) # {'D': 1, 'E': 1, 'F': 1}