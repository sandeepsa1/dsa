def lcs(arr1, arr2):
    m, n = len(arr1), len(arr2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the dp table
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            lcs_sequence.append(arr1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs_sequence[::-1]

# Example usage
arr1 = [1, 3, 4, 1, 2, 1, 3]
arr2 = [3, 4, 1, 2, 1, 3]
length, sequence = lcs(arr1, arr2)
print(f"Length of LCS: {length}")
print(f"LCS: {sequence}")