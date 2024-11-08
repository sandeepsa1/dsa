from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Step 1: Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Step 2: Initialize the queue with courses having in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    courses_taken = 0

    # Step 3: Process the courses
    while queue:
        course = queue.popleft()
        courses_taken += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return courses_taken == numCourses


numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(canFinish(numCourses, prerequisites))  # True