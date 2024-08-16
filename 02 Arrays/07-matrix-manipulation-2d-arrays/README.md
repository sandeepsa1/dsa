## Matrix Manipulation (2D Arrays)
Matrix manipulation refers to a wide range of operations that can be performed on 2D arrays (also known as matrices). These operations are fundamental in many areas, such as computer science, mathematics, physics, and engineering. Matrix manipulation involves various techniques to alter, analyze, or compute specific properties or results based on the elements of the matrix.<br/><br/>

Samples included here are;
1. <b>Rotate Matrix</b>: Rotates a given matrix by 90 degrees.
2. <b>Spiral Order Traversal</b>: Traverses a matrix in spiral order.


### 1. Rotate Matrix
The in-place method for rotating a matrix 90, 180 or 270 degrees clockwise is both time-efficient and space-efficient, making it a preferred approach when modifying the original matrix is acceptable.

1. Time complexity: <b>𝑂(n<sup>2</sub>)</b> because each element is visited twice—once during the transposition and once during the row reversal.
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
- 90 Degrees
   1. Transpose the matrix
   2. Reverse each row
- 180 Degrees
   1. Reverse each row
   2. Reverse the order of the rows
- 270 Degrees
   1. Transpose the matrix
   2. Reverse each column


### 2. Spiral Order Traversal
Spiral Order Traversal (also known as Spiral Matrix or Clockwise Spiral Traversal) is a technique to traverse a matrix in a spiral order, starting from the top-left corner and moving towards the center. This traversal pattern can be visualized as moving along the outer edges of the matrix and gradually spiraling inwards.

1. Time complexity: <b>𝑂(m * n)</b>, where 'm' is the number of rows and 'n' is the number of columns.
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Traverse the Top Row from the left to the right.
2. Traverse the Right Column from top to bottom.
3. Traverse the Bottom Row from right to left.
4. Traverse the Left Column from bottom to top.
5. Repeat the process for the next inner layer until all elements are visited.