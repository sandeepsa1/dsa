## Substring Problems
Substring problems are a class of problems in computer science where the goal is to find, manipulate, or analyze substrings within a larger string. A substring is a contiguous sequence of characters within a string. These problems are common in various domains, including text processing, bioinformatics, data compression, and more.<br/>

Algorithms included here are;
1. <b>Longest Common Substring</b>: Finds the longest substring that is common between two strings.
2. <b>Longest Palindromic Substring</b>: Finds the longest palindromic substring.


### 1. Longest Common Substring
The "Longest Common Substring" problem involves finding the longest substring that is common to two given strings. This is different from the "Longest Common Subsequence" problem, where the characters of the subsequence don't have to be contiguous.</br>

1. Time complexity: <b>𝑂(n * m)</b>
2. Space complexity: <b>𝑂(n * m)</b></br>

#### Steps
1. Create a 2D table 'dp' of size '(len(s1) + 1) x (len(s2) + 1)' initialized with zeros.
2. Initialize a variable 'max_len' to store the maximum length of the common substring found.
3. Initialize a variable 'end_index' to store the ending index of the longest common substring in 's1'.
4. Loop through the characters of 's1' and 's2'. For each pair '(i, j)', if 's1[i-1] == s2[j-1]', set 'dp[i][j] = dp[i-1][j-1] + 1'. Update 'max_len' and 'end_index' if 'dp[i][j]' exceeds 'max_len'.
5. The longest common substring can be extracted using the 'end_index' and 'max_len'.


### 2. Longest Palindromic Substring
The "Longest Palindromic Substring" problem involves finding the longest substring in a given string that reads the same forward and backward. A palindrome is a sequence of characters that looks the same when read from both directions.</br>

1. Time complexity: <b>𝑂(n<sup>2</sup>)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Iterate through each character in the string, treating it as the center of a palindrome.
2. Expand outward from the center to check for the longest palindrome with that center.
3. Consider both odd-length and even-length palindromes by expanding around a single character and a pair of characters.
4. Keep track of the longest palindrome found during the expansion.