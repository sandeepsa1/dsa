## String Pattern Matching Algorithms
Linked lists are a fundamental data structure in computer science, used to store a collection of elements in a linear order. Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each element (or node) contains a reference (or pointer) to the next element in the sequence.</br>

#### Types of Linked Lists
1. <b>Singly Linked List</b>: Each node points to the next node and the last node points to None.
2. <b>Doubly Linked List</b>: Each node points to both its next and previous nodes.
3. <b>Circular Linked List</b>: The last node points back to the first node, forming a circle.

#### Algorithms included here are;
1. <b>Traversal/Insert/Update/Delete</b>: Basic Linked List operations
2. <b>Reverse a Linked List</b>: Reverse the nodes in the linked list.
3. <b>Check if a Linked List is a Palindrome</b>: Determine if the linked list reads the same forward and backward.


### 1. Traversal/Insert/Update/Delete
Linked lists are flexible data structures that allow efficient insertions and deletions, especially when compared to arrays. Understanding how to traverse, insert, update, and delete elements in a linked list is fundamental to mastering data structures.

#### Steps
1. Traversal:
   - To traverse the linked list, start from the 'head' node and move to the next node using the 'next' pointer until you reach the end ('None').
   - This operation has a time complexity of O(n), where 'n' is the number of nodes in the linked list.
2. Insertion:
   - At the beginning: Create a new node and point its 'next' to the current 'head'. Then update the 'head' to this new node.
   - At the end: Traverse to the last node and update its 'next' pointer to the new node.
   - After a specific node: Create a new node, point its 'next' to the 'next' of the specific node, and update the 'next' of the specific node to this new node.
   - Each of these operations has a time complexity of O(1) for inserting at the beginning or after a specific node, but O(n) for inserting at the end (due to the need to traverse the list).
3. Updation:
   - To update a node, traverse to the desired position and change its 'data' field.
   - The time complexity is O(n) due to the need to traverse the list to find the node.
4. Deletion:
   - If the node to be deleted is the 'head', update the 'head' to the next node.
   - If the node is somewhere in the middle or end, traverse the list to find the node, then update the 'next' pointer of the previous node to bypass the node to be deleted.
   - This operation has a time complexity of O(n), as it may require traversing the list to find the node.


### 2. Reverse a Linked List
To reverse the nodes in a singly linked list, we'll need to change the direction of the 'next' pointers in each node so that they point to the previous node instead of the next one. We'll implement this using the functional approach without classes.</br>

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initial Setup:
   - We start with 'prev' set to 'None' and 'current' set to the head of the linked list.
2. Loop Through List: For each node:
   - Store the Next Node
   - Reverse the Pointer
   - Move Forward
3. Final Step:
   - Once the loop finishes, 'prev' will point to the new head of the reversed list.


### 3. Check if a Linked List is a Palindrome
To check if a linked list is a palindrome, we need to verify whether the elements of the linked list read the same forward and backward. Here's how you can implement this without using classes.</br>

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Find the Middle:
   - Use the two-pointer technique (slow and fast pointers) to find the middle of the linked list.
2. Reverse the Second Half:
   - Reverse the second half of the linked list.
3. Compare Both Halves:
   - Compare the first half with the reversed second half.