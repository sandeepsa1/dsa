## Binary Search Tree (BST)
A Binary Search Tree (BST) is a type of binary tree in which each node follows a specific ordering property:
- Left Subtree: All nodes in the left subtree of a node contain values less than the node’s value.
- Right Subtree: All nodes in the right subtree of a node contain values greater than the node’s value.
- This property holds for every node in the tree.

### Key Properties:
1. <b>Binary Structure</b>: Each node has at most two children (left and right).
2. <b>Search Efficiency</b>: The BST's structure allows for efficient searching, insertion, and deletion operations. In an ideal (balanced) BST, these operations take O(log n) time, where n is the number of nodes in the tree.
3. <b>Inorder Traversal</b>: Performing an inorder traversal on a BST yields the nodes in sorted order (from smallest to largest).

Different BST algorithms are;

1. <b>Insert, Update, Delete</b>: Insert, Update and Delete operations on a BST.
2. <b>Search</b>: Find if a value exists in the BST.
3. <b>Binary Search Tree Iterator</b>: Implement an iterator over a binary search tree (BST) with methods next() and hasNext().
4. <b>Kth Smallest Element in a BST</b>: Given a binary search tree, find the kth smallest element in it.
5. <b>Minimum Distance Between BST Nodes</b>: Given a BST, find the minimum absolute difference between the values of any two nodes.


### 1. Insert, Update, Delete
The Insert, Update, and Delete operations on a Binary Search Tree (BST) follow specific rules to maintain the BST property (i.e., for any node, all nodes in the left subtree are smaller, and all nodes in the right subtree are larger).

#### Steps
1. Insert
    1. Start from the root.
    2. Recursively compare the value to be inserted with the current node.
    3. If the value is smaller, move to the left subtree.
    4. If the value is larger, move to the right subtree.
    5. Insert the value when an empty spot ('-1' in this case) is found.
2. Update</br>
    The Update operation involves finding a node with a specific value and changing its value. In a standard BST, updating a node directly may break the BST property. Instead, the process involves deleting the node and reinserting the new value.
3. Delete</br>
    The Delete operation in a BST has three cases:
    1. Node has no children (leaf): Simply remove the node.
    2. Node has one child: Replace the node with its child.
    3. Node has two children: Replace the node with its inorder predecessor (maximum node in the left subtree) or inorder successor (minimum node in the right subtree), and recursively delete the predecessor/successor.


### 2. Search
To find if a value exists in a Binary Search Tree (BST), the search algorithm leverages the BST property, where:
- The left subtree contains values less than the current node.
- The right subtree contains values greater than the current node.
By comparing the target value with the current node and deciding which subtree to search, the algorithm can efficiently determine if the value exists.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Start at the root.
2. If the value is equal to the current node's value, the value exists in the BST.
3. If the value is less than the current node, search the left subtree.
4. If the value is greater than the current node, search the right subtree.
5. If you reach a null node ('-1' in this example), the value does not exist in the tree.


### 3. Binary Search Tree Iterator
To implement an iterator over a Binary Search Tree (BST), we need two primary methods:
- 'hasNext()': Returns 'True' if there are still nodes to be visited, and 'False' otherwise.
- 'next()': Returns the next smallest element in the BST, in inorder traversal order (since inorder traversal of a BST visits nodes in ascending order).

1. Time complexity: <b>𝑂(1)</b>
2. Space complexity: <b>𝑂(h)</b>, where h is the height of the tree

#### Steps
1. To achieve this, we use an iterative approach with a stack. The stack simulates the recursive nature of the inorder traversal, allowing us to "pause" and "resume" the traversal.
2. Initially, we push all left children of the root to the stack (this sets up the smallest element first).
3. Every call to  'next()' will:
    1. Pop the top element from the stack (this is the next smallest node).
    2. Push all left children of the right subtree of the popped node to the stack (if any).


### 4. Kth Smallest Element in a BST
To find the kth smallest element in a Binary Search Tree (BST), leverage the properties of inorder traversal. The inorder traversal of a BST visits the nodes in ascending order. Thus, performing an inorder traversal and counting the nodes visited allows us to identify the kth smallest element.

1. Time complexity: <b>𝑂(k)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Inorder Traversal:
    - Since the inorder traversal of a BST results in a sorted order of elements, we can traverse the tree and count the number of nodes visited until we reach the kth node.
2. Implement this either iteratively (using a stack) or recursively. The iterative approach will be more memory efficient for large trees.


### 5. Minimum Distance Between BST Nodes
In a Binary Search Tree, the inorder traversal visits the nodes in ascending order. Therefore, the smallest absolute difference between any two nodes in the tree will be between two consecutive nodes in the inorder traversal sequence.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Inorder Traversal:
    - Perform an inorder traversal of the BST to get the nodes in sorted order.
2. As traversed, compare the current node's value with the previous node's value, keeping track of the minimum difference between consecutive nodes.
3. This can be done either recursively or iteratively (using a stack).