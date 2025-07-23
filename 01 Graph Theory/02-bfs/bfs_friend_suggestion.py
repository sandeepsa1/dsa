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