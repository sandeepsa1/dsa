## Subarray and Substring Problems
Subarray and Substring Problems using Hash Table.

Samples included are;
1. <b>Subarray with Sum Zero</b>: Determine if a subarray with a sum of zero exists.
2. <b>Contiguous Array</b>: Given a binary array, find the maximum length of a contiguous subarray with an equal number of 0 and 1.


### 1. Subarray with Sum Zero
To determine if a subarray with a sum of zero exists in an array, use a hash table to track the cumulative sum as we iterate through the array.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Cumulative sum:
    - Calculate the cumulative sum at each index as we iterate through the array.
2. Check conditions:
    - If the cumulative sum is zero at any point, then there is a subarray starting from index 0 to the current index that sums to zero.
    - If the cumulative sum has been seen before, it means that the subarray between the previous occurrence of this sum and the current index sums to zero.
3. Use a hash table:
    - We use a hash table to store each cumulative sum and its index.


### 2. Contiguous Array
To find the maximum length of a contiguous subarray with an equal number of 0s and 1s in a binary array, use a hash map approach combined with a prefix sum technique.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Initialize a 'prefix_sum' to 0, which will keep track of the cumulative sum as we traverse the array.
2. Use a hash map ('prefix_sum_map') to store the first occurrence of each 'prefix_sum'. The key is the 'prefix_sum' and the value is the index at which it first occurs.
3. Iterate through the array, updating the 'prefix_sum' and checking the hash map:
    - If the same 'prefix_sum' has been seen before, the subarray between the previous occurrence and the current index has an equal number of 0s and 1s.
    - Update the maximum length of such subarray.
4. If 'prefix_sum' becomes zero, it means the entire subarray from the start has an equal number of 0s and 1s.