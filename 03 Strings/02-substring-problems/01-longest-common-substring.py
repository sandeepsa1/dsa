def longest_common_substring(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_len = 0
    end_index = 0
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
    
    longest_substring = s1[end_index - max_len:end_index]
    
    return max_len, longest_substring


s1 = "abcdef"
s2 = "zabcf"
length, substring = longest_common_substring(s1, s2)
print(f"Length: {length}, Substring: '{substring}'")