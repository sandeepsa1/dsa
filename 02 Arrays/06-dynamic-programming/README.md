## Dynamic Programming
Dynamic Programming (DP) is an algorithmic technique used for solving complex problems by breaking them down into simpler subproblems. It is particularly effective for optimization problems where the problem can be divided into overlapping subproblems that can be solved independently.<br/><br/>

Samples included here are;
1. <b>Maximum Subarray Sum (Kadane’s Algorithm)</b>: Finds the contiguous subarray with the maximum sum.
2. <b>Longest Increasing Subsequence</b>: Finds the longest increasing subsequence in an array.
3. <b>Longest Common Subsequence</b>: Finds the longest common subsequence between two arrays.


### 1. Maximum Subarray Sum (Kadane’s Algorithm)
Kadane’s Algorithm is a popular method used to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum. It works in linear time, making it highly efficient.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialization:
   - Set two variables: 'max_current' and 'max_global'. Both are initialized to the first element of the array.
   - Initialize 'start', 'end' to keep track of the beginning and end indices of the maximum sum subarray.
   - Initialize 's' to keep track of the potential start of a new subarray.
2. Iterate through the array:
   - For each element in the array starting from the second element:
      - Update 'max_current' to be the maximum of the current element itself or the current element plus 'max_current'.
      - If the current element alone is greater than the current subarray sum ('max_current'), start a new subarray by updating 's' to the current index.
      - Update 'max_global' and the 'start' and 'end' indices whenever a new maximum is found.
3. Return the result:
   - Return 'max_global' and the subarray using the 'start' and 'end' indices.


### 2. Longest Increasing Subsequence
The Longest Increasing Subsequence (LIS) problem involves finding the longest subsequence of a given sequence where the elements are in strictly increasing order. The subsequence doesn't need to be contiguous, but it must maintain the relative order of elements from the original sequence.</br></br>

The solution provided here is a combination of dynamic programming and binary search which provides a better performance.

1. Time complexity: <b>𝑂(n log n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Maintain a list sub where 'sub[i]' contains the smallest possible last element of an increasing subsequence of length 'i+1'.
2. Keep an additional list 'prev_indices' to track the predecessors of each element in the sequence.
3. Keep a list 'indices' to track the indices of elements in 'sub'.
4. Reconstruct the LIS by backtracking through the 'prev_indices' list.


### 3. Longest Common Subsequence
The Longest Common Subsequence (LCS) problem involves finding the longest subsequence that is present in both of the given sequences (arrays, strings, etc.), where the subsequence need not be contiguous but must maintain the relative order of elements. The most common and efficient way to solve the LCS problem is by using dynamic programming.

1. Time complexity: <b>𝑂(m * n)</b>, where m and n are the lengths of arr1 and arr2.
2. Space complexity: <b>𝑂(m * n)</b></br>, due to the storage of the DP table.

#### Steps
1. Initialize a DP Table:
   - Create a 2D array 'dp' with dimensions '(len(arr1)+1) x (len(arr2)+1)'.
   - Initialize the first row and first column to '0', as the LCS of any sequence with an empty sequence is '0'.
2. Fill the DP Table:
   - For each pair of elements '(arr1[i-1], arr2[j-1]), if they are equal, set dp[i][j] = dp[i-1][j-1] + 1'.
   - If they are not equal, set 'dp[i][j] = max(dp[i-1][j], dp[i][j-1])'.
3. Reconstruct the LCS:
   - Start from 'dp[len(arr1)][len(arr2)]' and backtrack to reconstruct the LCS.


### Problems Where Dynamic Programming is Useful
1. <b>Knapsack Problem</b>: Maximizing the value of items in a knapsack without exceeding its weight capacity.
2. <b>Longest Common Subsequence (LCS)</b>: Finding the longest subsequence common to two sequences.
3. <b>Shortest Path Problems</b>: Finding the shortest path in a graph with certain constraints.
4. <b>Edit Distance</b>: Finding the minimum number of edits required to convert one string into another.
5. <b>Coin Change Problem</b>: Finding the minimum number of coins needed to make a certain amount of money.