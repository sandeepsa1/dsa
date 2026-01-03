import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    heap = [(0, k)]
    dist = {}

    while heap:
        time, node = heapq.heappop(heap)

        if node in dist:
            continue

        dist[node] = time

        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (time + w, nei))

    if len(dist) != n:
        return -1

    return max(dist.values())


times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]
n = 4
k = 2

print(networkDelayTime(times, n, k)) # 2