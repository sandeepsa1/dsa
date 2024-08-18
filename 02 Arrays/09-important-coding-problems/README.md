## Important Coding Problems in Arrays
Some of the important and most common coding problems related to Arrays Data Structure.<br/><br/>

1. <b>Product of Array Except Self</b>: Given an array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
2. <b>Maximum Product Subarray</b>: Find the contiguous subarray within an array which has the largest product.
3. <b>Find Minimum in Rotated Sorted Array</b>: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element.
4. <b>Search in Rotated Sorted Array</b>: Search for a target value in a rotated sorted array.
5. <b>Merge Intervals</b>: Given a collection of intervals, merge all overlapping intervals.


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

### 3. Find Minimum in Rotated Sorted Array
To solve the problem of finding the minimum element in a rotated sorted array, a modified binary search can be used. The key insight is that even though the array has been rotated, it remains partially sorted, which allows us to use binary search to find the minimum element efficiently.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Check Middle Element:
   - Compare the middle element to the element at the right end of the array.
   - If 'nums[mid] > nums[right]', then the minimum element lies in the right half (since the smallest element must be in the unsorted part).
   - If 'nums[mid] <= nums[right]', then the minimum element lies in the left half or could be the middle element itself.
2. Adjust the Search Range:
   - Narrow down the search range by adjusting the 'left' and 'right' pointers based on the comparison.
3. End Condition:
   - The loop continues until the 'left' pointer meets the 'right' pointer. At this point, the minimum element is found.

### 4. Search in Rotated Sorted Array
A modified binary search similar to the approach used for finding the minimum element can be used. The key difference is that instead of just locating the minimum, we need to find the target value. Since the array is rotated but still partially sorted, we can use this property to determine which part of the array to search next.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initial Pointers:
   - The left and right pointers start at the beginning and end of the array.
2. Binary Search:
   - Calculate 'mid'.
   - Determine if the left or right half of the array is sorted.
   - Use the sorted half to adjust 'left' and 'right'.
3. End Condition:
   - If the target is found, its index is returned; if not, '-1' is returned.

### 5. Merge Intervals
Given an array of intervals where each interval is represented as a pair of integers '[start, end]', merge all overlapping intervals and return the result as a list of merged intervals.

1. Time complexity: <b>𝑂(n log n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Sort the Intervals:
   - First, sort the intervals based on their starting times. This makes it easier to detect overlaps since any overlapping intervals must be consecutive in the sorted list.
2. Merge Intervals:
   - Initialize a result list with the first interval.
   - Iterate through the sorted intervals:
      - If the current interval overlaps with the last interval in the result list, merge them by updating the end of the last interval in the result list to the maximum end of both intervals.
      - If the current interval does not overlap, simply add it to the result list.
3. Return the Result