## Sort, Reverse, Split, Reorder and Rotate of Linked Lists
Sort, Reverse, Split, Reorder and Rotate operations on Linked Lists data structure.

#### Algorithms included here are;
1. <b>Sort List</b>: Sort a linked list in O(n log n) time and constant space complexity.
2. <b>Remove Duplicates from Sorted List</b>: Remove all elements from a sorted linked list that have duplicates.
3. <b>Reverse Nodes in k-Group</b>: Reverse the nodes of a linked list k at a time and return its modified list.
4. <b>Split Linked List in Parts</b>: Split the linked list into k consecutive linked list parts.
5. <b>Reorder List</b>: Reorder a linked list in a specific pattern.
6.  <b>Rotate List</b>: Rotate the linked list to the right by k places.


### 1. Sort List
To sort a linked list in O(n log n) time and O(1) (constant) space, use the Merge Sort algorithm. Merge Sort is a divide-and-conquer algorithm that is well-suited for sorting linked lists because it doesn’t require random access to elements, making it efficient with linked list operations.

1. Time complexity: <b>O(n log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Divide:
   - Split the linked list into two halves until each half contains a single node.
2. Conquer:
   - Recursively sort both halves.
3. Combine:
   - Merge the two sorted halves to produce a sorted linked list.


### 2. Remove Duplicates from Sorted List
To remove duplicates from a sorted linked list, traverse the list and compare each node with the next one. If the current node's value is the same as the next node's value, you skip the next node by adjusting the next pointer of the current node.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Traversing the List:
   - The 'remove_duplicates' function traverses the linked list using a 'current' pointer.
   - For each node, it checks if the current node's value is the same as the next node's value.
2. Skipping Duplicates:
   - If the values are the same, the 'next' pointer of the current node is adjusted to skip the duplicate node, effectively removing it from the list.
3. Continue Traversing:
   - If the values are different, the 'current' pointer moves to the next node.


### 3. Reverse Nodes in k-Group
To reverse nodes in a linked list in groups of k, approach the problem by recursively or iteratively reversing the nodes in each group and then linking them back together.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Check if there are 'k' nodes:
   - Start from the current node and check if there are 'k' nodes available. If there aren't, return the node as it is.
2. Reverse the 'k' nodes:
   - Reverse the nodes in this group.
3. Recurse for the next group:
   - Once a group is reversed, recurse for the next 'k' nodes and link them together.


### 4. Split Linked List in Parts
To split a linked list into 'k' consecutive parts, the idea is to distribute the nodes as evenly as possible across the parts. If the total number of nodes is not divisible by 'k', some parts will have one more node than others.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(k)</b></br>

#### Steps
1. Calculate the length of the linked list.
2. Determine the size of each part:
   - Calculate the minimum size each part should have.
   - Determine how many parts should have an extra node.
3. Split the linked list into 'k' parts accordingly.


### 5. Reorder List
To reorder a linked list in a specific pattern, where the pattern involves rearranging the list in the form of L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ..., follow below steps:

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Find the middle of the linked list using the slow and fast pointer technique.
2. Reverse the second half of the linked list.
3. Merge the two halves by alternating nodes from each half.


### 6. Rotate List
To rotate a linked list to the right by 'k' places, the idea is to move the last 'k' nodes to the front of the list. 

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Find the length of the linked list.
2. Compute the effective rotation using 'k % length'.
3. Identify the new tail and new head after the rotation.
4. Perform the rotation by adjusting the pointers.