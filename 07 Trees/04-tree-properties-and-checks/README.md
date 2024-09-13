## Tree Properties and Checks
Finding the tree properties and performing below checks on trees.

1. <b>Height of a Tree</b>: Compute the height (or depth) of a tree.
2. <b>Diameter of a Tree</b>: Find the length of the longest path between any two nodes in a tree.
3. <b>Diameter of Binary Tree</b>: Given a binary tree, find the length of the diameter of the tree.
4. <b>Maximum Depth of Binary Tree</b>: Given the root of a binary tree, return its maximum depth.
5. <b>Balanced Tree Check</b>: Determine if a binary tree is balanced, i.e., the height difference between left and right subtrees of any node is at most 1.
6. <b>Check for Symmetry</b>: Determine if a binary tree is symmetric around its center
7. <b>Sum of Left Leaves</b>: Given a binary tree, find the sum of all left leaves.


### 1. Height of a Tree
To compute the height (or depth) of a tree, define height as the number of edges on the longest path from the root node to a leaf node. The height of a leaf node is 0, and the height of an empty tree is considered to be -1.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Start at the root.
2. Recursively compute the height of the left and right subtrees.
3. The height of the current node is the maximum of the heights of its subtrees, plus 1.


### 2. Diameter of a Tree
The problem of finding the length of the longest path between any two nodes in a tree is also known as finding the diameter of the tree. The diameter of a tree is the number of edges in the longest path between any two nodes. The path may or may not pass through the root, and the length is counted in terms of the number of edges.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
The diameter of a tree can be computed using a depth-first search (DFS) by calculating the longest path through each node. The longest path through any node is the sum of the heights of its left and right subtrees. The largest such sum for all nodes gives the diameter of the tree.
1. Start at the root and recursively calculate the height of each subtree.
2. At each node, compute the diameter as the sum of the heights of the left and right subtrees.
3. Keep track of the maximum diameter encountered.


### 3. Diameter of Binary Tree
To find the diameter of a binary tree, which is the length of the longest path between any two nodes, follow the same general approach as outlined  in the above code.


### 4. Maximum Depth of Binary Tree
To find the maximum depth of a binary tree, calculate the longest path from the root node to a leaf node. The depth of a binary tree is the number of edges from the root node to the deepest leaf. If we consider the root node to have a depth of 1, we define the maximum depth recursively.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. If the current node is 'None' (i.e., an empty subtree), return '0'.
2. Recursively calculate the depth of the left and right subtrees.
3. The depth of the current node is the maximum of the depths of the left and right subtrees, plus 1.


### 5. Balanced Tree Check
A binary tree is balanced if the height difference between the left and right subtrees of every node is at most 1. This means for every node in the tree:
- The left subtree's height and the right subtree's height differ by no more than 1.
- Both left and right subtrees are themselves balanced.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. For each node, recursively compute the height of its left and right subtrees.
2. If at any node the height difference between the left and right subtree is more than 1, the tree is not balanced.
3. If the subtrees of all nodes are balanced and the height difference at each node is at most 1, the tree is balanced.


### 6. Check for Symmetry
To determine if a binary tree is symmetric around its center, check if the left and right subtrees are mirror images of each other. In simpler terms, for the tree to be symmetric:
- The left subtree of the root should be a mirror of the right subtree.
- For any pair of nodes on the left and right sides, their values should be the same, and their respective children should also be mirrors of each other (i.e., the left child of the left node should match the right child of the right node, and vice versa).

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
Solve this problem recursively by comparing two nodes:
1. If both nodes are 'None', they are symmetric (base case).
2. If one node is 'None' and the other is not, they are not symmetric.
3. If both nodes have the same value, check if:
    - The left child of the left node is symmetric with the right child of the right node.
    - The right child of the left node is symmetric with the left child of the right node.


### 7. Sum of Left Leaves
To find the sum of all left leaves in a binary tree, traverse the tree and identify which nodes are left leaves. A left leaf is a node that:
- Is a left child of its parent.
- Does not have any children (i.e., it is a leaf node).

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(h)</b>

#### Steps
1. Traverse the binary tree recursively or iteratively.
2. For each node, check if its left child is a leaf.
3. If it is, add its value to the sum.
4. Continue the traversal to the right and left subtrees.