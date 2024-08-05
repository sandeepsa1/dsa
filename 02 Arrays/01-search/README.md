## Array Search Algorithms
There are several algorithms used to search for elements within arrays. These can be broadly categorized into two types: linear search algorithms and binary search algorithms. Important array search algorithms are;
1. Linear Search: Simple but inefficient for large arrays.
2. Binary Search: Efficient for sorted arrays.
3. Interpolation Search: Efficient for uniformly distributed sorted arrays.
4. Jump Search: Efficient for sorted arrays with a predictable jump size.
5. Exponential Search: Efficient for unbounded/infinite lists.


### 1. Linear Search
Linear search is the simplest search algorithm. It sequentially checks each element of the array until a match is found or the whole array has been searched.

1. Time complexity: <b>𝑂(n)</b> where 𝑛 is the number of elements in the array.
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Start from the first element and move to the next.
2. Compare each element with the target value.
3. If a match is found, return the index.
4. If no match is found after checking all elements, return -1.


### 2. Binary Search
Binary search is an efficient algorithm for finding an element in a sorted array. It works by repeatedly dividing the search interval in half.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Begin with the whole array.
2. Compare the target value to the middle element of the array.
3. If the target value equals the middle element, return its index.
4. If the target value is less than the middle element, repeat the search on the left half.
5. If the target value is greater than the middle element, repeat the search on the right half.
6. If the interval is empty, the target is not in the array, return -1.


### 3. Interpolation Search
Interpolation search is an improvement over binary search for instances where the values in a sorted array are uniformly distributed. It attempts to predict where the target might be based on the value.

1. Time complexity: <b>𝑂(log log n)</b> in the best case, <b>𝑂(n)</b> in the worst case.
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Calculate the position using the formula. <b>pos = left + (   (target−arr[left]) × (right−left)    /    (arr[right] - arr[left])   )</b>
2. Compare the target value with the element at the calculated position.
3. If the target value equals the element at the position, return the index.
4. If the target value is less, repeat the search on the left sub-array.
5. If the target value is greater, repeat the search on the right sub-array.
6. If the target is not found, return -1.


### 4. Jump Search
Jump search is a search algorithm for sorted arrays. It works by dividing the array into blocks of a fixed size and performing a linear search within the blocks.

1. Time complexity: <b>𝑂(√n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Determine the block size to be <b>√n</b>.
2. Jump through the array by the block size until the target value is found or a value greater than the target is encountered.
3. If a match is found, return the index.
4. Perform a linear search within the block where the target value might be.


### 5. Exponential Search
Exponential search is a combination of binary search and a search algorithm for sorted arrays. It is particularly useful for unbounded or infinite lists.

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Start with the first element.
2. Exponentially increase the index to find the range where the target value may reside.
3. Perform a binary search within that range.