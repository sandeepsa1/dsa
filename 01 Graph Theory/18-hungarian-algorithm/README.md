## Hungarian Algorithm
The Hungarian algorithm, also known as the Kuhn-Munkres algorithm, is used for solving the assignment problem, which involves finding the optimal way to assign <b>n</b> tasks that involves a cost(weight), to <b>n</b> agents such that the total cost is minimized (or total profit is maximized). It works on a cost matrix where each element represents the cost of assigning a particular agent to a particular task.</br></br>

<b>Hungarian Algorithm</b> is suitable for finding minimum cost or maximum profit matching in <b>weighted bipartite graphs</b>. Whereas;
<b>Hopcroft-Karp Algorithm</b> is suitable for finding maximum cardinality matching in <b>unweighted bipartite graphs</b>.

1. Time complexity: <b>𝑂(n<sup>3</sup>>)</b>
2. Space complexity: <b>𝑂(n<sup>2</sup>>)</b>


### Steps of the Hungarian Algorithm
1. Subtract Row Minimums:
   - Subtract the smallest value in each row from all the elements of the row.
2. Subtract Column Minimums:
   - Subtract the smallest value in each column from all the elements of the column.
3. Cover All Zeros with a Minimum Number of Lines:
   - Use a combination of horizontal and vertical lines to cover all zeros in the matrix with the minimum number of lines.
4. Check Optimality:
   - If the minimum number of lines is equal to the number of rows (or columns), an optimal assignment exists among the zeros.
   - If not, modify the matrix and repeat from step 3.
5. Adjust the Matrix:
   - Find the smallest value not covered by any line.
   - Subtract this value from all uncovered elements and add it to elements covered by two lines.

### Uses
1. <b>Task Assignment</b>: Assigning jobs to workers in a way that minimizes total cost or maximizes efficiency.
2. <b>Resource Allocation</b>: Allocating resources (e.g., machines, materials) to different tasks or projects.
3. <b>Matching Problems</b>: Used in various matching problems in graph theory, such as finding a perfect matching in a weighted bipartite graph.
4. <b>Assignment in Sports</b>: Assigning players to positions, teams to fixtures, or officials to games.

https://www.youtube.com/watch?v=FCaD34z--bY