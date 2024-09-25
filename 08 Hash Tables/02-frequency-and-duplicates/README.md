## Frequency and Duplicates
Operations like counting the frequency of elements or finding duplicates.

#### Basic Operations
1. <b>Counting Frequencies</b>: Count the frequency of elements in a collection.
2. <b>Finding Duplicates</b>: Identify duplicates in an array or list.
3. <b>Top K Frequent Elements</b>: Find the k most frequent elements in an array.
4. <b>First Unique Character in a String</b>: Given a string, find the first non-repeating character in it and return its index.


### 1. Counting Frequencies
To count the frequency of elements using a hash table approach, use a dictionary in Python. Dictionaries are implemented as hash tables in Python, allowing efficient insertion and lookup operations, typically in O(1) time complexity.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>


### 2. Finding Duplicates
To identify duplicates in an array or list, we can also use a hash table (i.e., a dictionary in Python) to efficiently track the elements. The approach is to iterate through the list, adding each element to the hash table as we go. If an element is already present in the hash table, it's a duplicate.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>


### 3. Top K Frequent Elements
To find the k most frequent elements in an array, use a hash table to count the frequency of each element. Then, use a max-heap or sorting to efficiently extract the k elements with the highest frequency.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n log n)</b>

#### Steps
1. Count the frequency of elements using a hash table.
2. Sort or use a heap to get the k most frequent elements.


### 4. First Unique Character in a String
To find the first non-repeating character in a string and return its index, use a hash table to count the frequency of each character. After counting the characters, iterate through the string again to find the first character with a frequency of 1.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Count the frequency of each character in the string using a hash table.
2. Find the first non-repeating character by checking which character appears only once, in the order they appear in the string.