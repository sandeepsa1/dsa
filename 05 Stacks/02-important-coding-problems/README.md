## Important Coding Problems in Linked Lists
Some of the important and most common coding problems related to Linked Lists.<br/>

Some codes implemented are;
1. <b>Next Greater Element - One Array</b>: Find the next greater element for each element in an array.
2. <b>Next Greater Element - Two Arrays</b>: Given two arrays (without duplicates). For each element in the first array, find the next greater element in the second array.
3. <b>Stock Span Problem</b>: Calculate the span of stock prices for each day.
4. <b>Daily Temperatures</b>: Given a list of daily temperatures, return a list such that, for each day in the input, how many days to wait until a warmer temperature.
5. <b>Largest Rectangle in Histogram</b>:  Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.
6. <b>Trapping Rain Water</b>: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



### 1. Next Greater Element - One Array
Finding the next greater element for each element in an array is a common problem that can be solved efficiently using a stack-based approach. The goal is to find the next greater element for every element in the array, meaning the first element to the right of the current element that is larger than the current element.</br>
The "Next Greater Element" problem specifically requires finding the first greater element to the right of the current element in the array, not just any greater element.

#### Steps
1. Initialize an empty stack and an array 'nge[]' of the same size as the input array to store the results. Initialize all elements of 'nge[]' to '-1'.
2. Traverse the input array from right to left.
    - For each element 'arr[i]':
        - While the stack is not empty and the top element of the stack is less than or equal to 'arr[i]', pop the stack (since the top element cannot be the next greater element for any previous elements).
        - If the stack is not empty after the above step, the top element of the stack is the next greater element for 'arr[i]'.
        - Push 'arr[i]' onto the stack.
3. Return the array 'nge[]'.


### 2. Next Greater Element - Two Arrays
To solve this, use a combination of a hash map and a stack. This problem is a variation of the "Next Greater Element" problem but with the additional requirement that the next greater elements must be determined from a different array.

#### Steps
1. Initialize an empty stack and an empty hash map 'nge_map'.
2. Traverse 'nums2' from right to left.
    - For each element 'num' in 'nums2':
        - While the stack is not empty and the top element of the stack is less than or equal to 'num', pop the stack (since the top element cannot be the next greater element for any previous elements).
        - If the stack is not empty after the above step, the top element of the stack is the next greater element for 'num'.
        - Map the current element 'num' to its next greater element in 'nge_map'.
        - Push 'num' onto the stack.
3. Result:
    - For each element in 'nums1', look up its next greater element in 'nge_map'. If it exists, return it; otherwise, return '-1'.


### 3. Stock Span Problem
Given an array of stock prices where each element represents the price of the stock on a particular day, you need to calculate the span of stock prices for each day.

#### Steps
1. The idea is to maintain a stack such that prices corresponding to indices stored in the stack are in decreasing order.


### 4. Daily Temperatures
The problem asks for a list of daily temperatures and requires calculating the number of days you need to wait for a warmer temperature. If there is no future day with a warmer temperature, the result for that day should be '0'.

#### Steps
1. Initialize:
    - Create a list 'answer' of zeros with the same length as 'temperatures' to store results.
    - Use a stack to store indices of temperatures.
2. Process Temperatures:
    - Loop through each temperature using its index 'i'.
    - While the stack isn't empty and the current temperature is warmer than the temperature at the index on top of the stack:
        - Pop the index from the stack.
        - Set the difference between the current index and the popped index in 'answer'.
    - Push the current index 'i' onto the stack.
3. Return Results.


### 5. Largest Rectangle in Histogram
To find the area of the largest rectangle in a histogram, use a stack-based approach. This method efficiently calculates the maximum area by leveraging the stack to store indices of histogram bars.


### 6. Trapping Rain Water
To solve the problem of computing how much water can be trapped in an elevation map after raining, use a two-pointer approach. The idea is to use two pointers to traverse the elevation map from both ends towards the center. As the pointers move inward, keep track of the maximum heights encountered from both sides and use them to calculate the trapped water.