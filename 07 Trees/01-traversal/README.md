## Tree Traversal Algorithms
Tree traversal is the process of visiting each node in a tree data structure exactly once in a specific order. A tree is made up of nodes connected by edges, where each node contains data, and a traversal algorithm defines the sequence in which the nodes are accessed.</br>
Different tree traversal algorithms are;

1. <b>Inorder Traversal</b>: Traverse the tree in the order: left subtree, root, right subtree.
2. <b>Preorder Traversal</b>: Traverse the tree in the order: root, left subtree, right subtree.
3. <b>Postorder Traversal</b>: Traverse the tree in the order: left subtree, right subtree, root.
4. <b>Level Order Traversal</b>: Traverse the tree level by level, from left to right.


### 1. Inorder Traversal
Inorder Traversal is a tree traversal algorithm that visits the nodes of a binary tree in a specific order: left subtree → root → right subtree. This traversal is commonly used for binary search trees (BST) because it retrieves the nodes' values in sorted order.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Traverse the left subtree by recursively applying inorder traversal.
2. Visit the root node.
3. Traverse the right subtree by recursively applying inorder traversal.


### 2. Preorder Traversal
In preorder traversal, the nodes of a tree are visited in the order; Root node, Left subtree and Right subtree.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Visit the root node.
2. Traverse the left subtree by recursively applying preorder traversal.
3. Traverse the right subtree by recursively applying preorder traversal.


### 3. Postorder Traversal
In postorder traversal, the nodes of a tree are visited in the order; Left subtree, Right subtree and Root node.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Traverse the left subtree by recursively applying postorder traversal.
2. Traverse the right subtree by recursively applying postorder traversal.
3. Visit the root node.


### 4. Level Order Traversal
Level Order Traversal is a tree traversal algorithm that visits nodes level by level, starting from the root, and proceeding from left to right at each level. This traversal is typically implemented using a queue (FIFO) to keep track of the nodes to be visited.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Start at the root node.
2. Visit all nodes at the current level, from left to right.
3. Move to the next level and repeat the process until all nodes are visited.


### Comparison of Different Types of Tree Traversals
| Traversal     | Use Cases                                                                                                     |
| ------------- |---------------------------------------------------------------------------------------------------------------|
| Inorder       | Retrieving nodes in sorted order from a BST, to validate if a binary tree is a valid BST                      |
| Preorder      | Tree construction, evaluate prefix expressions in expression trees, copying trees since root is copied first  |
| Postorder     | Deleting trees because child nodes are deleted first, evaluate postfix expressions, bottom-up calculations    |
| Level Order   | Breadth-First Search when exploring nodes level by level, shortest paths, completeness of tree, print trees   |