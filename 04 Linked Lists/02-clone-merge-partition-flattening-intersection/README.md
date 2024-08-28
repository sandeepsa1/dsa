## Clone, Merge, Flattening, Partition and Intersection of Linked Lists
Clone, Merge, Flattening, Partition and Intersection operations on Linked Lists data structure.

#### Algorithms included here are;
1. <b>Clone a Linked List with Random Pointers</b>: Create a deep copy of a linked list where each node has an additional random pointer.
2. <b>Merge Two Sorted Lists</b>: Merge two sorted linked lists into a single sorted list.
3. <b>Merge K Sorted Lists</b>: Merge multiple sorted linked lists into a single sorted list.
4. <b>Partition List</b>: Rearrange the list so that all nodes less than a given value come before all nodes greater than or equal to the value.
5. <b>Flatten a Multilevel Doubly Linked List</b>: Flatten a multilevel doubly linked list where nodes may have a child pointing to a separate doubly linked list.
6.  <b>Find Intersection Node</b>: Find the node at which two linked lists intersect.


### 1. Clone a Linked List with Random Pointers
To clone a linked list where each node has an additional random pointer, create a deep copy of the list, ensuring that both the 'next' and 'random' pointers are correctly set in the new list.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. First Pass - Copy Nodes and Insert Them Next to Original Nodes:
   - Create a new node for each original node and place it right next to the original node in the linked list.
2. Second Pass - Assign Random Pointers:
   - Set the 'random' pointers of the newly created nodes using the interleaved structure.
3. Third Pass - Separate the Lists:
   - Detach the new nodes from the original list to form the cloned list.


### 2. Merge Two Sorted Lists
To merge two sorted linked lists into a single sorted list, use a two-pointer technique to compare the nodes from both lists and build a new sorted list by linking the nodes in the correct order.

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialize Pointers:
   - Use two pointers to traverse the two lists. We'll also have a pointer to keep track of the new list's tail.
2. Compare Nodes:
   - At each step, compare the nodes pointed to by the two pointers and add the smaller node to the new list.
3. Handle Remaining Nodes:
   - Once one of the lists is fully traversed, append the remaining nodes from the other list to the new list.


### 3. Merge K Sorted Lists
To merge multiple sorted linked lists into a single sorted list, utilize a min-heap (or priority queue) approach to efficiently find the smallest element among the heads of the k lists at each step. This approach works well for merging k sorted lists because it allows to always choose the smallest element from the remaining lists and add it to the merged list.

1. Time complexity: <b>𝑂(N log k)</b>, where N is the total number of nodes across all k lists.
2. Space complexity: <b>𝑂(k)</b></br>

#### Steps
1. Min-Heap Initialization:
   - Push the head of each of the k linked lists into a min-heap.
2. Heap Operations:
   - Extract the smallest node from the heap and add it to the merged list. If this node has a next node, push it into the heap.
3. Repeat:
   - Continue the process until the heap is empty.


### 4. Partition List
To solve the problem of partitioning a linked list around a given value 'x', use two pointers to create two separate lists: one for nodes with values less than 'x' and another for nodes with values greater than or equal to 'x'. After traversing the original list, concatenate these two lists to form the partitioned linked list.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialize Two Dummy Nodes:
   - Create two dummy nodes, 'before_head' and 'after_head', which will act as the heads of the "before" and "after" lists. Use 'before' and 'after' pointers to build these lists.
2. Traverse the List:
   - Traverse the original linked list. For each node:
      - If the node's value is less than 'x', append it to the "before" list.
      - If the node's value is greater than or equal to 'x', append it to the "after" list.
3. Concatenate the Lists:
   - Finally, link the "before" list to the "after" list and set the last node of the "after" list to 'None'.


### 5. Flatten a Multilevel Doubly Linked List
Given a multilevel doubly linked list where in addition to the next and previous pointers, each node has a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure. Flatten the list so that all the nodes appear in a single-level, doubly linked list.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Iterative Depth-First Search (DFS):
   - Use an iterative DFS approach with a stack to traverse through the multilevel doubly linked list.
2. Stack Operations:
   - Push the 'next' pointer onto the stack if it exists, to return to after finishing the child list.
   - If a node has a child, link the child list into the main list and move to the child.
   - Once a child list is exhausted, pop from the stack to return to the previous list.
3. Update Pointers:
   - As we traverse the list, update the 'next' and 'prev' pointers to maintain the flattened structure.


### 6. Find Intersection Node
To find the intersection node of two singly linked lists, where the two lists converge at a certain node, use an approach that involves aligning the lengths of the two lists and then traversing them simultaneously to find the intersection.

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Determine Lengths:
   - First, determine the lengths of both linked lists.
2. Align Starts:
   - Adjust the starting point of the longer list so that both lists have the same number of nodes to traverse.
3. Traverse Together:
   - Traverse both lists simultaneously until the nodes are the same, which indicates the intersection point.