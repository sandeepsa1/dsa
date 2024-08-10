## Sliding Window Technique
The sliding window technique is an efficient way to solve problems involving subarrays or sublists by maintaining a window (a contiguous sequence of elements) that slides over the input data structure. It is commonly used to solve problems involving subarrays, substrings, or other contiguous subsequences in arrays or strings.<br/><br/>

Samples included here are;
1. <b>Maximum Sum Subarray of Size K</b>: Finds the maximum sum of any subarray of size K.
2. <b>Longest Substring Without Repeating Characters</b>: Finds the longest substring without repeating characters.


### 1. Maximum Sum Subarray of Size K
To find the maximum sum of a subarray of size 𝐾 in an array, we can use the sliding window technique. This approach allows to efficiently calculate the sum of subarrays of size 𝐾 by updating the sum as the window move across the array, rather than recalculating the sum from scratch for each subarray.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialize:
   - Initialize the sum of the first 𝐾 elements.
2. Slide the Window:
   - Slide the window across the array by adding the next element and removing the first element of the previous window.
3. Find Maximum Sum:
   - Keep track of the maximum sum encountered during this process.

#### Uses
This algorithm is useful in situations where you need to find an optimal subarray in terms of sum, such as in financial data analysis (finding the best period of stock price gains) or in signal processing.


### 2. Longest Substring Without Repeating Characters
To find the longest substring without repeating characters, sliding window technique combined with a hash set (or dictionary) can be used.

1. Time complexity: <b>𝑂(n)</b>, where 𝑛 is the length of the string.
2. Space complexity: <b>𝑂(min(m,n))</b></br>, where 𝑚 is the size of the character set (e.g., 26 for lowercase English letters).

#### Steps
1. Initialize Two Pointers:
   - Start with two pointers, 'start' and 'end', both set to the beginning of the string. These pointers represent the current window of characters being considered.
2. Expand the Window:
   - Move the 'end' pointer to the right to expand the window and include more characters.
3. Check for Repeating Characters:
   - If the character at 'end' is not in the current window, add it to the window.
   - If the character is already in the window, move the 'start' pointer to the right until the repeating character is removed from the window.
4. Track the Maximum Length:
   - Throughout this process, keep track of the maximum length of a substring without repeating characters.
5. Continue Until the End:
   - Repeat the above steps until the 'end' pointer reaches the end of the string.