from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Initialize the graph
    graph = defaultdict(set)
    indegree = defaultdict(int)
    
    # Step 2: Initialize indegree for all unique characters
    for word in words:
        for char in word:
            indegree[char] = 0
    
    # Step 3: Build the graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    indegree[word2[j]] += 1
                break
        else:
            if len(word2) < len(word1):
                return ""
    
    # Step 4: Perform BFS (Kahn's Algorithm) for topological sorting
    queue = deque([char for char in indegree if indegree[char] == 0])
    alien_order = []
    
    while queue:
        char = queue.popleft()
        alien_order.append(char)
        
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(alien_order) < len(indegree):
        return ""
    
    # Step 5: Return the topologically sorted order
    return "".join(alien_order)


words = ["wrt", "wrf", "er", "ett", "rftt"]
result = alien_order(words)
print("Alien Language Order:", result)