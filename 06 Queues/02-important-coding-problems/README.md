## Important Coding Problems related to Queues
Some of the important and most common coding problems related to Queues.<br/>

Some codes implemented are;
1. <b>Sliding Window Maximum</b>: Find the maximum value in each sliding window of size k in an array.
2. <b>LRU Cache</b>: Design a Least Recently Used (LRU) cache.
3. <b>Rotten Oranges</b>: Determine the time taken for all oranges to rot given that a rotten orange affects adjacent oranges.
4. <b>Moving Average from Data Stream</b>: Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
5. <b>Number of Recent Calls</b>:  Write a class that counts the number of recent requests within a certain time frame.
6. <b>Course Schedule</b>: Determine if you can finish all courses given the prerequisites.



### 1. Sliding Window Maximum
Given an array 'nums' and a window size 'k', the task is to find the maximum value in each sliding window of size 'k' as it moves from the start to the end of the array.

#### Steps
1. Initialize a deque:
    - The deque will store indices of array elements.
The elements corresponding to these indices are in non-increasing order.
2. Iterate over the array:
    - For each element:
        - Remove indices from the deque that are out of the bounds of the current sliding window.
        - Remove elements from the deque that are smaller than the current element since they can never be the maximum in future windows.
        - Append the current index to the deque.
        - The front of the deque contains the index of the maximum element in the current window.
3. Extract results:
    - After processing the first 'k' elements, start adding the maximum element (front of the deque) to the result for each window.


### 2. LRU Cache
The task is to design a data structure that follows the Least Recently Used (LRU) cache eviction policy. The cache should support the following operations:
    - get(key): Retrieve the value associated with the key if it exists, otherwise return -1.
    - put(key, value): Insert or update the value associated with the key. If the cache reaches its capacity, it should evict the least recently used item before inserting a new item.

#### Steps
1. Deque (doubly linked list):
    - Maintain the order of usage of elements. The most recently used element will be at one end (usually the front), and the least recently used will be at the other end (usually the back).
2. Hash Map (Dictionary):
    - Store the actual key-value pairs for quick access.
    - The key maps to the node in the deque, allowing O(1) access and updates.


### 3. Rotten Oranges
Given a matrix where each cell represents the state of an orange:
    - 0: Empty cell.
    - 1: Fresh orange.
    - 2: Rotten orange.
A rotten orange will affect all its adjacent (up, down, left, right) fresh oranges, causing them to rot in one minute. The task is to determine the minimum time required for all oranges to rot. If not all oranges can rot, return '-1'.

#### Steps
1. Initialize a queue:
    - Store the position of all rotten oranges and start the BFS process from these positions.
2. Track time:
    - Keep a count of the time taken for all oranges to rot. Each layer in BFS corresponds to one minute.
3. Process fresh oranges:
    - For every rotten orange in the queue, check its four adjacent cells (up, down, left, right). If any adjacent cell has a fresh orange, it becomes rotten, and we add this new rotten orange to the queue.
4. Check for remaining fresh oranges:
    - After BFS, if there are any fresh oranges left that couldn't rot, return '-1'.
5. Edge cases:
    - If there are no fresh oranges at the beginning, return '0'.


### 4. Moving Average from Data Stream
Given a stream of integers and a window size 'k', we need to calculate the moving average of the integers within the sliding window of size 'k'. This involves maintaining a sliding window of the last 'k' elements from the stream and calculating the average of these elements as new integers arrive.

#### Steps
1. Initialize an empty queue and a variable to store the current sum of elements in the queue.
2. For each new integer:
    - Add the integer to the queue.
    - Add the integer to the current sum.
    - If the size of the queue exceeds k, remove the oldest element and adjust the sum.
3. Calculate the moving average by dividing the sum by the number of elements in the queue.


### 5. Number of Recent Calls
Design a system that counts the number of recent requests or calls within a specific time frame, typically a sliding window of a certain duration (e.g., the last 3000 milliseconds). Each time a new call is made, the system should return the number of calls that were made within that time frame.

#### Steps
1. Initialize an empty queue to store the timestamps of the calls.
2. For each new call:
    - Add the timestamp to the queue.
    - Remove all timestamps from the front of the queue that are older than the specified time frame.
    - Return the size of the queue, which will represent the number of recent calls.


### 6. Course Schedule
The problem "Determine if you can finish all courses given the prerequisites" can be modeled as a graph problem, specifically detecting cycles in a Directed Acyclic Graph (DAG). The courses can be represented as nodes, and the prerequisites as directed edges between these nodes.

#### Steps
1. Model the courses as a graph:
    - Represent each course as a node.
    - Use an adjacency list to represent the graph where each node points to its dependent course.
2. Track the in-degree of each course:
    - The in-degree of a node is the number of prerequisites for that course.
3. Use a queue to perform a BFS:
    - Add all nodes with an in-degree of 0 (no prerequisites) to the queue.
    - Process each node by removing it from the queue, reducing the in-degree of its dependent courses.
    - If a dependent course’s in-degree becomes 0, add it to the queue.
4. If all courses are processed, return true (i.e., it's possible to finish all courses).
    - If there are courses that still have non-zero in-degrees, it means there is a cycle in the graph, and return false.