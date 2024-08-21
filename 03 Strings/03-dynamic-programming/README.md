## Substring Problems
Dynamic Programming (DP) is an algorithmic technique used for solving complex problems by breaking them down into simpler subproblems. It is particularly effective for optimization problems where the problem can be divided into overlapping subproblems that can be solved independently.<br/>

Algorithms included here are;
1. <b>Longest Common Subsequence</b>: Finds the longest common subsequence between two strings.
2. <b>Edit Distance (Levenshtein Distance)</b>: Computes the minimum number of operations to transform one string into another.


### 1. Longest Common Subsequence
The "Longest Common Subsequence" (LCS) problem involves finding the longest subsequence that appears in the same order in both given strings. A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</br>

Steps are exactly same as finding the Longest Common Subsequence of arrays.

#### Key Difference between Longest Common Substring and Longest Common Subsequence
    - <b>Longest Common Subsequence</b>: The LCS is a sequence that appears in the same order in both strings, but not necessarily consecutively. For example, the LCS of "abcde" and "ace" is "ace".
    - <b>Longest Common Substring</b>: The longest common substring is a sequence that appears as a consecutive block in both strings. For example, the longest common substring of "abcde" and "abfce" is "ab".

### 2. Edit Distance (Levenshtein Distance)
The goal is to find the minimum number of operations required to transform one string into another. The allowed operations are:
1. Insertion of a character.
2. Deletion of a character.
3. Substitution of a character.</br>

1. Time complexity: <b>𝑂(m * n)</b>
2. Space complexity: <b>𝑂(m * n)</b></br>

#### Steps
1. Initialization:
    - If either string is empty, the only option is to insert all characters of the other string. Therefore, 'dp[i][0] = i' and 'dp[0][j] = j'.
2. Filling the DP Table:
    - For each pair of characters in 'word1' and 'word2', decide whether to insert, delete, or substitute a character.
    - If 'word1[i-1] == word2[j-1]', no operation is needed: 'dp[i][j] = dp[i-1][j-1]'.
    - Otherwise, choose the minimum of the three operations:
        - Insert: 'dp[i][j-1] + 1'
        - Delete: 'dp[i-1][j] + 1'
        - Substitute: 'dp[i-1][j-1] + 1'