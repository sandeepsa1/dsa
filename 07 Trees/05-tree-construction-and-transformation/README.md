## Tree Construction and Transformation
Construct or transform trees.

1. <b>Convert BST to Sorted Doubly Linked List</b>: Convert a binary search tree to a sorted doubly linked list in-place.
2. <b>Convert Sorted Array to Binary Search Tree</b>: Given an integer array where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
3. <b>Invert Binary Tree</b>: Given the root of a binary tree, invert the tree (flip it upside down).
4. <b>Construct Binary Tree from Preorder and Inorder Traversal</b>: Given preorder and inorder traversal of a tree, construct the binary tree.


### 1. Convert BST to Sorted Doubly Linked List
To convert a Binary Search Tree (BST) into a Sorted Doubly Linked List, perform an inorder traversal of the BST. The inorder traversal will visit nodes in sorted order (left subtree, root, right subtree), and while doing so, link the nodes together into a doubly linked list.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Start an inorder traversal from the root.
2. For each node:
    - Link it to the previous node (set its left pointer to the previous node).
    - Set the previous node's right pointer to the current node.
3. Update the previous node to the current node.
4. Return the head of the linked list at the end.


### 2. Convert Sorted Array to Binary Search Tree
To convert a sorted array into a balanced Binary Search Tree (BST), use a recursive approach where the middle element of the array becomes the root of the tree. The elements to the left of the middle element form the left subtree, and the elements to the right form the right subtree. This guarantees that the resulting BST is height-balanced.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(log n)</b>

#### Steps
1. Find the middle element of the array.
2. Recursively build the left subtree using the elements before the middle element.
3. Recursively build the right subtree using the elements after the middle element.
4. Return the root of the tree.


### 3. Invert Binary Tree
Inverting a binary tree involves swapping the left and right children of every node in the tree. This transforms the tree into its mirror image.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. For each node, invert its left and right subtrees.
2. Swap the left and right children.
3. Return the root of the tree after inverting.


### 4. Construct Binary Tree from Preorder and Inorder Traversal
To construct a binary tree from preorder and inorder traversal sequences, we use the following properties of these traversals:
1. <b>Preorder Traversal</b>: The first element is always the root of the tree.
2. <b>Inorder Traversal</b>: The elements to the left of the root (from preorder) are in the left subtree, and the elements to the right are in the right subtree.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Use the first element from the preorder sequence to find the root of the tree.
2. Find the position of this root in the inorder sequence. Elements to the left of this position form the left subtree, and elements to the right form the right subtree.
3. Recursively build the left and right subtrees using the corresponding portions of the preorder and inorder sequences.