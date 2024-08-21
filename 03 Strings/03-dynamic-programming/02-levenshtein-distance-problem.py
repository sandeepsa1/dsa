def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    return dp[m][n]


word1 = "horse"
word2 = "ros"
print(f"The minimum number of operations required: {min_distance(word1, word2)}")

word1 = "intention"
word2 = "execution"
print(f"The minimum number of operations required: {min_distance(word1, word2)}") 