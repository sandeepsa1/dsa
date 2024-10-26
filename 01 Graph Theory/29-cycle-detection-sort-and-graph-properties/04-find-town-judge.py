def findJudge(n, trust):
    if n == 1:
        return 1
    
    trust_count = [0] * (n + 1)
    
    for a, b in trust:
        trust_count[a] -= 1
        trust_count[b] += 1
    
    for i in range(1, n + 1):
        if trust_count[i] == n - 1:
            return i
    
    return -1


print(findJudge(4, [[1, 4], [2, 4], [3, 4]]))  # 4

n = 5
trust = [
    [1, 3],
    [2, 3],
    [4, 3],
    [5, 3],
    [2, 4],
    [4, 5]
]
print(findJudge(n, trust)) # 3