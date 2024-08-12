## Divide and Conquer Technique
Divide and Conquer is a fundamental algorithmic technique used to solve problems by breaking them down into smaller, more manageable subproblems, solving each subproblem individually, and then combining their solutions to address the original problem. This method is effective for a wide range of problems, including sorting, searching, and optimization.<br/><br/>

Samples included here are;
1. <b>Closest Pair of Points</b>: Find the pair of points that are closest to each other in terms of Euclidean distance.
2. <b>Find K-th Largest Element - Quickselect</b>: Uses a modified quicksort algorithm to find the k-th largest element.


### 1. Closest Pair of Points
Given a set of points in a two-dimensional plane, find the pair of points that are closest to each other in terms of Euclidean distance.

1. Time complexity: <b>𝑂(n log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Divide:
   - Sort the points by their x-coordinates.
   - Divide the set of points into two halves.
2. Conquer:
   - Recursively find the closest pair of points in each half.
3. Combine:
   - Find the closest pair of points that span the two halves.
   - This involves checking points that lie within a certain vertical strip (width determined by the minimum distance found in the recursive calls).


### 2. Find K-th Largest Element - Quickselect
Quickselect is closely related to the Quicksort algorithm. While Quicksort is a sorting algorithm that fully sorts an array, Quickselect only partially sorts it to find the k-th largest (or smallest) element, which allows it to be more efficient.

1. Time complexity: <b>𝑂(n)</b>, but in the worst case (e.g., if bad pivots are consistently chosen), it can degrade to <b>𝑂(n<sup>2</sup>)</b>, which is very rare.
2. Space complexity: <b>𝑂(1)</b></br>

#### How this Works
1. Partitioning:
   - Similar to Quicksort, Quickselect chooses a pivot element from the array.
   - The array is then partitioned such that all elements less than the pivot are moved to the left of the pivot, and all elements greater than the pivot are moved to the right.
2. Selection:
   - After partitioning, the pivot element is in its final sorted position in the array.
   - If the pivot’s position is the k-th position, then it is the k-th largest (or smallest) element, and the algorithm returns it.
   - If the pivot’s position is greater than k, the algorithm recursively selects the k-th largest element from the left subarray.
   - If the pivot’s position is less than k, the algorithm recursively selects the k-th largest element from the right subarray (adjusting k to account for the elements that have been discarded).