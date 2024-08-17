## Important Coding Problems in Arrays
Some of the important and most common coding problems related to Arrays Data Structure.<br/><br/>

1. <b>Product of Array Except Self</b>: Given an array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
2. <b>Maximum Product Subarray</b>: Find the contiguous subarray within an array which has the largest product.


### 1. Product of Array Except Self
The goal is to create an array where each element at index 'i' is the product of all elements in the original array except the one at 'i'. The challenge is to do this without using division and in 'O(n)' time complexity.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
The problem can be solved by breaking it into two passes:
1. Left Pass:
   - Traverse the array from left to right, and for each element at index 'i', calculate the product of all elements to the left of 'i'.
2. Right Pass:
   - Traverse the array from right to left, and for each element at index 'i', calculate the product of all elements to the right of 'i', while multiplying it with the product from the left pass.


### 2. Maximum Product Subarray
The "Maximum Product Subarray" problem requires finding the contiguous subarray within an array that has the largest product of its elements. This problem is somewhat similar to the Maximum Subarray Sum problem but requires additional considerations due to the nature of multiplication, particularly with positive, negative, and zero values.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialize Variables:
   - 'max_product' to store the maximum product found so far.
   - 'min_product' to store the minimum product (because a negative number could flip this into a maximum later).
   - 'result' initialized to the first element of the array (since the array must contain at least one element).
2. Iterate Through the Array:
   - For each element, update 'max_product' and 'min_product'.
   - If the current element is negative, swap 'max_product' and 'min_product'.
   - Update 'max_product' to be the maximum of the current element or the current element times 'max_product'.
   - Similarly, update 'min_product' to be the minimum of the current element or the current element times 'min_product'.
   - Update 'result' to store the maximum value of 'result' and 'max_product'.
3. Return Result