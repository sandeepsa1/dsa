from collections import defaultdict, deque

def can_finish_courses(num_courses, prerequisites):
    # Step 1: Create graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Step 2: Initialize the queue with courses having in-degree of 0
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])

    # Step 3: Perform BFS
    processed_courses = 0
    while queue:
        current = queue.popleft()
        processed_courses += 1

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1  # Reduce in-degree
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if we were able to process all courses
    return processed_courses == num_courses


num_courses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]  # 0 -> 1 -> 2 -> 3
print(can_finish_courses(num_courses, prerequisites))  # True

num_courses = 4
prerequisites = [[1, 0], [0, 1]]  # Cycle between course 0 and 1
print(can_finish_courses(num_courses, prerequisites))  # False