## Special Algorithms and Operations on Trees
Construct or transform trees.

1. <b>Find Path Sum</b>: Given a binary tree and a sum, determine if there is a root-to-leaf path that sums up to the given sum.
2. <b>Find Duplicate Subtrees</b>: Given a binary tree, find all duplicate subtrees and return a list of their roots.
3. <b>Recover Binary Search Tree</b>: Two nodes of a binary search tree (BST) are swapped by mistake. Recover the tree without changing its structure.
4. <b>Tree to String - Serialize and Deserialize</b>: Convert a tree to a string and back to a tree.


### 1. Find Path Sum
To solve the problem of determining if there exists a root-to-leaf path in a binary tree where the sum of node values equals a given target sum, use a recursive approach.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Start at the root of the tree and at each node, subtract the value of the node from the given sum.
2. Recursively check the left and right subtrees with the updated sum.
3. If a leaf node is reached and the remaining sum equals the value of the leaf node, return 'True'.
4. If no such path is found, return 'False'.


### 2. Find Duplicate Subtrees
To find all duplicate subtrees in a binary tree and return a list of their roots, serialize each subtree and use a dictionary to keep track of the frequency of each subtree structure.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>


### 3. Recover Binary Search Tree
To recover a binary search tree (BST) where two nodes have been swapped by mistake, identify the two nodes that are out of place and then swap them back to restore the BST properties.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Perform an inorder traversal.
2. Track the two swapped nodes during the traversal.
3. Swap the values of the two nodes to restore the BST property.


### 4. Tree to String - Serialize and Deserialize
To convert a tree to a string and back to a tree, use a serialization and deserialization approach. The tree will be serialized into a string format and deserialized back into its original structure.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>