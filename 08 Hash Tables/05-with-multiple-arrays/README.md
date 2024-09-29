## Advanced Problems with Multiple Arrays
Advanced Problems with Multiple Arrays using Hash Table.

Samples included are;
1. <b>Happy Number</b>: A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
2. <b>Intersection of Two Arrays</b>: Given two arrays, write a function to compute their intersection.
3. <b>Longest Consecutive Sequence</b>: Find the length of the longest consecutive elements sequence.
4. <b>Four Sum II</b>: Given four lists of integers, compute how many tuples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] == 0.


### 1. Happy Number
A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(log n)</b>

#### Steps
1. Create a helper function to compute the sum of the squares of the digits of the current number.
2. Use a set to track numbers that was already seen to detect cycles. If the number reappears, it means in a loop and n is not a happy number.
3. Keep calculating the sum of the squares of the digits of the number until:
    - Get 1 (happy number).
    - Detect a cycle (not a happy number).


### 2. Intersection of Two Arrays
To compute the intersection of two arrays, find the common elements that appear in both arrays.

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Create a hash map to store the frequency of elements in the first array.
2. Iterate through the second array and check if the element exists in the hash map and has a non-zero count.
3. Add the element to the result and reduce its count in the hash map.
4. Return the result list.


### 3. Longest Consecutive Sequence
To find the length of the longest consecutive elements sequence in an unsorted array of integers, use a set for quick lookup.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Convert the array into a set.
2. For each number, check if it’s the start of a sequence (i.e., num - 1 is not in the set).
3. If it is the start of a sequence, count the consecutive elements from that number.
4. Return the maximum length of any sequence found.


### 4. Four Sum II
This problem is a variation of the 4Sum II problem where there are four integer lists A, B, C, and D. Find how many tuples (i, j, k, l) such that: <b>A[i] + B[j] + C[k] + D[l] == 0</b>.

1. Time complexity: <b>𝑂(n<sup>2</sup>>)</b>
2. Space complexity: <b>𝑂(n<sup>2</sup>>)</b>

#### Steps
1. Create a hash map to store the sum of pairs from lists A and B along with their frequencies.
2. Iterate over all pairs from lists C and D and check if the negative of their sum exists in the hash map.
3. Return the total count of such tuples.