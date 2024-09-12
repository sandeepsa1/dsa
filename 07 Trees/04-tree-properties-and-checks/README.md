## Tree Properties and Checks
Finding the tree properties and performing below checks on trees.

1. <b>Height of a Tree</b>: Compute the height (or depth) of a tree.
2. <b>Diameter of a Tree</b>: Find the length of the longest path between any two nodes in a tree.
3. <b>Diameter of Binary Tree</b>: Given a binary tree, find the length of the diameter of the tree.
4. <b>Maximum Depth of Binary Tree</b>: Given the root of a binary tree, return its maximum depth.


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