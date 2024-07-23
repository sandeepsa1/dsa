import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph.get(current, []):
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

def heuristic(a, b):
    # Example heuristic: Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

'''graph = { # A simple graph
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1), ((0, 2), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1), ((2, 0), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((2, 1), 1), ((1, 2), 1)],
    (1, 2): [((1, 1), 1), ((0, 2), 1), ((2, 2), 1)],
    (2, 0): [((1, 0), 1), ((2, 1), 1)],
    (2, 1): [((2, 0), 1), ((1, 1), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1), ((1, 2), 1)]
}

start = (0, 0)
goal = (2, 2)'''

graph = { # A graph with different weights and obstacles (Some nodes not accessible).
    (0, 0): [((0, 1), 1), ((1, 0), 4)],
    (0, 1): [((0, 0), 1), ((0, 2), 2)],
    (0, 2): [((0, 1), 2), ((0, 3), 1), ((1, 2), 3)],
    (0, 3): [((0, 2), 1), ((1, 3), 2)],
    (1, 0): [((0, 0), 4), ((2, 0), 1)],
    (1, 2): [((0, 2), 3), ((1, 3), 2), ((2, 2), 1)],
    (1, 3): [((0, 3), 2), ((1, 2), 2), ((2, 3), 3)],
    (2, 0): [((1, 0), 1), ((3, 0), 2)],
    (2, 2): [((1, 2), 1), ((3, 2), 3)],
    (2, 3): [((1, 3), 3), ((3, 3), 1)],
    (3, 0): [((2, 0), 2), ((3, 1), 4)],
    (3, 1): [((3, 0), 4), ((3, 2), 5)],
    (3, 2): [((2, 2), 3), ((3, 3), 1), ((3, 1), 5)],
    (3, 3): [((2, 3), 1), ((3, 2), 1)]
}

start = (0, 0)
goal = (3, 3)
path = a_star(graph, start, goal, heuristic)
print("Path found:", path)