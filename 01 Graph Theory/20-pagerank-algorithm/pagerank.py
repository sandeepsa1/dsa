def pagerank(graph, damping_factor=0.85, max_iterations=100, tol=1.0e-6):
    n = len(graph)
    rank = {node: 1 / n for node in graph}
    new_rank = rank.copy()

    for iteration in range(max_iterations):
        for node in graph:
            rank_sum = 0
            for incoming in graph:
                if node in graph[incoming]:
                    rank_sum += rank[incoming] / len(graph[incoming])
            new_rank[node] = (1 - damping_factor) / n + damping_factor * rank_sum

        # Check convergence
        converged = True
        for node in graph:
            if abs(new_rank[node] - rank[node]) > tol:
                converged = False
                break

        if converged:
            break

        rank = new_rank.copy()

    return new_rank

graph = {
    0: [1, 2],
    1: [2],
    2: [0],
    3: [0, 1, 2]
}

pagerank_result = pagerank(graph)
print("PageRank Results:", pagerank_result)