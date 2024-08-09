## Two-Pointer Technique
The two-pointer technique is a common algorithmic approach used to solve problems that involve searching, sorting, or manipulating data in arrays, linked lists, or strings. It involves using two pointers (or indices) to traverse the data structure simultaneously, often from different directions or at different speeds. This technique is particularly useful for problems that require finding pairs, subarrays, or managing elements relative to each other.<br/><br/>

Samples included here are;
1. <b>Two Sum Problem</b>: Finds two numbers in an array that sum up to a target value.
2. <b>K Sum Problem</b>: Finds <b>K</b> numbers in an array that sum up to a target value.
3. <b>Array duplicate removal</b>: Remove duplicate elements from an array.


### 1. Two Sum Problem
The Two Sum Problem is an algorithmic problem where the goal is to find two distinct numbers in an array that sum up to a specific target value.

1. Time complexity: <b>𝑂(n)</b> where 𝑛 is the number of elements in the array.
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Initialize a Hash Map:
   - Create an empty dictionary to store numbers from the array as keys and their corresponding indices as values.
2. Iterate Through the Array:
   - For each number 'num' in the array, calculate its 'complement' by subtracting 'num' from the target: 'complement = target - num'.
3. Check if the Complement Exists:
   - Check if the complement is already in the dictionary.
   - If it is, return the indices of the complement and the current number.
   - If it isn't, store the current number in the dictionary along with its index.
4. Return Result


### 2. K-Sum Problem
The K-Sum problem is a generalization of the Two Sum problem. The goal is to find 'k' distinct numbers in an array that sum up to a specific target value. The problem becomes increasingly complex as 'k' increases.

1. Time complexity: <b>𝑂(n<sup>k-1</sup>)</b>
2. Space complexity: <b>𝑂(k)</b></br>

#### Steps
1. Sorting the Array:
   - The array is first sorted to help handle duplicates and to make the recursive logic more straightforward.
2. Recursive Function:
   - The main function 'find_k_sum' initializes the results list and calls the helper function 'k_sum_recursive' to start the recursive process.
3. Base Case (k = 1):
   - When 'k' equals 1, just check if the remaining target exists in the subarray starting from start. If it does, the function appends the current combination (path) with this number to the results list.
4. Recursive Case (k > 1):
   - When k is greater than 1, the function iterates through the array starting from 'start' up to 'len(arr) - k + 1'. Duplicates are skipped and recursive calls are made. The recursion continues until it reaches the base case.
5. Recursive Case (k > 1):
   - When k is greater than 1, the function iterates through the array starting from 'start' up to 'len(arr) - k + 1'. Duplicates are skipped and recursive calls are made. The recursion continues until it reaches the base case.
6. Return Results


### 3. Array duplicate removal
To remove duplicates from a sorted array in place, two-pointer technique can be used. This approach is efficient and modifies the array in place without requiring extra space for another array.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Initialization:
   - 'unique_index' is used to keep track of the position where the next unique element should be placed.
2. Iterate Through the Array:
   - Start from the second element ('i = 1') and compare each element with the element at 'unique_index'.
   - If the current element is different from the element at 'unique_index', update 'unique_index' and place the current element at this position.
3. Return the Length:
   - After processing all elements, the array from the start to 'unique_index + 1' contains all unique elements. The function returns 'unique_index + 1', which is the length of the array with unique elements.