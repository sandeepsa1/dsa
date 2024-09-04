## Queues
A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed, similar to a line of people waiting for service: the person who arrives first is served first.

#### Algorithms included here are;
1. <b>Enqueue, Dequeue, Front, isEmpty</b>: Basic Queue operations
2. <b>Circular Queue</b>: Implement a queue that wraps around when it reaches the end.
3. <b>Queue using Stacks</b>: Implement a queue using two stacks.
4. <b>Generate Binary Numbers</b>: Generate binary numbers from 1 to n using a queue.
5. <b>Level Order Traversal of Binary Tree</b>: Traverse a binary tree level by level.


### 1. Enqueue, Dequeue, Front, isEmpty
Enqueue, Dequeue, Front/Peek and isEmpty are the basic operations that can be performed on a queue.


### 2. Circular Queue
A circular queue is a linear data structure that uses a fixed-size array, and the queue wraps around when the end of the array is reached. This allows for efficient use of space by reusing the slots that become vacant after dequeuing.


### 3. Queue using Stacks
This implementation uses two stacks to simulate the FIFO behavior of a queue. Elements are moved from 'stack1' to 'stack2' only when 'stack2' is empty during a dequeue operation, ensuring the operations are efficient.


### 4. Generate Binary Numbers
To generate binary numbers from 1 to n using a queue, follow below approach:

#### Steps
1. Initialize the Queue:
   - Start by initializing a queue and enqueue the first binary number "1".
2. Dequeue and Generate:
   - For each step, dequeue the front element, print it, and then generate its next two binary numbers by appending "0" and "1" to it.
3. Enqueue New Numbers:
   - Enqueue the newly generated binary numbers back into the queue.
4. Repeat:
   - Repeat the above steps until you generate 'n' binary numbers.


### 5. Level Order Traversal of Binary Tree
To traverse a binary tree level by level (also known as Breadth-First Search (BFS) or Level Order Traversal), use a queue to process each level of the tree one by one.

#### Steps
1. Initialize the Queue:
   - Start by initializing a queue and enqueue the root node of the binary tree.
2. Process Each Node:
   - Dequeue the front node from the queue.
   - Process the node (e.g., print its value).
   - Enqueue its left and right children (if they exist) into the queue.
3. Repeat:
   - Continue until the queue is empty, which means all nodes have been processed.