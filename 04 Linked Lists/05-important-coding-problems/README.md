## Important Coding Problems in Linked Lists
Some of the important and most common coding problems related to Linked Lists.<br/>

Some codes implemented are;
1. <b>Add Two Numbers</b>: Add two numbers represented by linked lists. The digits are stored in reverse order.
2. <b>Swap Nodes in Pairs</b>: Swap every two adjacent nodes in a linked list.
3. <b>Odd Even Linked List</b>: Group all odd nodes together followed by the even nodes in a linked list.


### 1. Add Two Numbers
To add two numbers represented by linked lists, where each node contains a single digit, and the digits are stored in reverse order (e.g., '2 -> 4 -> 3' represents the number 342), sum the numbers digit by digit. If the sum of two digits exceeds 9, we carry over the extra digit to the next addition.

#### Steps
1. Initialize pointers for both linked lists and a carry variable.
2. Traverse both linked lists, adding corresponding digits along with any carry from the previous step.
3. Handle any remaining carry after the lists are fully traversed.


### 2. Swap Nodes in Pairs
To swap every two adjacent nodes in a linked list, follow these steps:

#### Steps
1. Use a dummy node to simplify edge cases like swapping the head node.
2. Iterate through the linked list two nodes at a time.
3. Swap the nodes by adjusting the pointers.
4. Move to the next pair and repeat until the end of the list.


### 3. Odd Even Linked List
To group all odd nodes together followed by all even nodes in a linked list, follow these steps:

#### Steps
1. Initialize two pointers: one for odd-indexed nodes and one for even-indexed nodes.
2. Traverse the linked list, separating the nodes into odd and even groups.
3. Connect the odd list to the even list at the end.