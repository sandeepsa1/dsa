Lowest Common Ancestor (LCA)
The Lowest Common Ancestor (LCA) of two nodes in a Binary Tree is the lowest (deepest) node that has both nodes as descendants. In simpler terms, given two nodes in a binary tree, the LCA is the farthest node from the root that is an ancestor of both nodes.

1. <b>LCA of a Binary Tree</b>: Find the lowest common ancestor of two nodes in a tree.
2. <b>LCA of a Binary Search Tree</b>: Given a binary search tree (BST) and two nodes, find their LCA.


### 1. LCA of a Binary Tree
To find the LCA of two nodes in a general binary tree, use a recursive approach. In a binary tree, unlike a Binary Search Tree (BST), the ordering property cannot be leveraged, so need to traverse the tree and look for the nodes directly.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Recursive Traversal:
    - Start from the root and recursively search for the two nodes in both the left and right subtrees.
2. Base Case:
    - If you reach a leaf node or find one of the target nodes, return that node.
3. LCA Condition:
    - At any node, if one node is found in the left subtree and the other is found in the right subtree, then the current node is the LCA. If both nodes are found in one subtree, the LCA will be in that subtree.


### 2. LCA of a Binary Search Tree
To find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST), use the properties of the BST:
    - In a BST, the values of the nodes in the left subtree are smaller than the value of the root.
    - The values of the nodes in the right subtree are larger than the value of the root.

1. Time complexity: <b>𝑂(h)</b>
2. Space complexity: <b>𝑂(1)</b>

#### Steps
1. Start from the root.
2. Compare the values of the two nodes with the current node:
    - If both nodes are smaller, move to the left subtree.
    - If both nodes are larger, move to the right subtree.
    - If the values split (one smaller, one larger), or if the current node matches one of the nodes, the current node is the LCA.