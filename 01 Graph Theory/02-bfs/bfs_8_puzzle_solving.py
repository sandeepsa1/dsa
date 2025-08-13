from collections import deque

def bfs_puzzle(start, goal):
    def get_neighbors(state):
        neighbors = []
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dr, dc in moves:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_index = nr * 3 + nc
                new_state = list(state)
                # swap blank with target
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))
        return neighbors

    queue = deque([(start, [])])  # (state, moves)
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]  # return full path to goal
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))
    
    return None


start_state = (1, 2, 3,
               4, 0, 5,
               6, 7, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

solution_path = bfs_puzzle(start_state, goal_state)

if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves.")
    # for state in solution_path:
    #     print(f"{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")
else:
    print("No solution found.")