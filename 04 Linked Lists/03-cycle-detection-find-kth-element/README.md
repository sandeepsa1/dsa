## Cycle Detection and find Kth Element
1. <b>Detect a Cycle and Find the Starting Node of the Cycle</b>: Check if the linked list contains a cycle. Locate the node where the cycle begins.
2. <b>Find Kth to Last Element</b>: Retrieve the k-th to last element in the linked list.


### 1. Detect a Cycle and Find the Starting Node of the Cycle
To detect a cycle in a linked list, a common and efficient approach is to use Floyd’s Cycle-Finding Algorithm (Steps 1 and 2), also known as the "Tortoise and Hare" algorithm. This algorithm uses two pointers moving at different speeds to determine whether a cycle exists.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(k)</b>

#### Steps
1. Two Pointers: Use two pointers, 'slow' and 'fast'.
   - 'slow' moves one step at a time.
   - 'fast' moves two steps at a time.
2. Cycle Detection:
   - If there is no cycle, the 'fast' pointer will eventually reach the end ('None').
   - If there is a cycle, the 'fast' pointer will eventually meet the 'slow' pointer.
3. Find the Start of the Cycle:
   - Once slow and fast pointers meet, reset one of the pointers to the head.
   - Move both pointers one step at a time. The node where they meet again will be the start of the cycle.
4. Collect the Cycle Nodes:
   - Start from the detected cycle start node and traverse until you return to the same node, collecting all nodes in between.


### 2. Find Kth to Last Element
To find the k-th to last element in a linked list, use the "two-pointer" technique. The idea is to have two pointers separated by 'k' nodes, so that when the second pointer reaches the end of the list, the first pointer is at the k-th to last element.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b>

#### Steps
1. Initialize Two Pointers:
   - Start with both pointers at the head of the linked list.
2. Move the Second Pointer:
   - Move the second pointer 'k' nodes ahead.
3. Move Both Pointers:
   - Move both pointers one step at a time. When the second pointer reaches the end, the first pointer will be at the k-th to last element.