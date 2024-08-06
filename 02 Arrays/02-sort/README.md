## Array Sort Algorithms
Important array sort algorithms are;
1. Bubble Sort: Simple but inefficient; suitable for small datasets.
2. Insertion Sort: Efficient for small datasets and mostly sorted arrays; simple to implement.
3. Selection Sort: Simple but inefficient; good for small datasets and cases where memory writes are a concern.
4. Merge Sort: Efficient and stable; good for large datasets; requires additional space.
5. Quick Sort: Efficient on average; widely used in practice; in-place but not stable.
6. Heap Sort: Efficient and in-place; does not require additional space; not stable.


### 1. Bubble Sort
Bubble sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

1. Time complexity: <b>𝑂(n<sup>2</sup>)</b> where 𝑛 is the number of elements in the array.
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Start at the beginning of the array.
2. Compare each pair of adjacent elements.
3. Swap them if they are in the wrong order.
4. Repeat the process for all elements until no swaps are needed.


### 2. Insertion Sort
Insertion sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

1. Time complexity: <b>𝑂(n<sup>2</sup>)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Iterate from the second element to the last element.
2. For each element, compare it with elements in the sorted part of the array.
3. Insert it into its correct position.


### 3. Selection Sort
Selection sort divides the input list into two parts: the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty, and the unsorted part is the entire list. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.

1. Time complexity: <b>𝑂(n<sup>2</sup>)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Find the minimum element in the unsorted part.
2. Swap it with the leftmost unsorted element.
3. Move the boundary of the sorted part one element to the right.
4. Repeat until the array is sorted.


### 4. Merge Sort
Merge sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

1. Time complexity: <b>𝑂(n log n)</b> in all cases.
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Divide the unsorted list into 𝑛 sublists, each containing one element.
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.


### 5. Quick Sort
Quick sort is an efficient, in-place, divide and conquer, comparison-based sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

1. Time complexity: <b>𝑂(n log n)</b> on average, <b>𝑂(n<sup>2</sup>)</b> in the worst case.
2. Space complexity: <b>𝑂(log n)</b></br>

#### Steps
1. Choose a pivot element from the array.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than or equal to the pivot.
3. Recursively apply the above steps to the sub-arrays.

### 6. Heap Sort
Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the same process for the remaining elements.

1. Time complexity: <b>𝑂(n log n)</b> in all cases.
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of the heap by 1.
3. Heapify the root of the tree.
4. Repeat the above steps while the size of the heap is greater than 1.