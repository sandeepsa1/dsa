## Basic Hash Table Operations
A hash table (or hash map) is a data structure that stores key-value pairs. It allows for fast insertion, deletion, and lookup operations. The core idea behind a hash table is to use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

#### Example
Let’s say you want to store a list of student names and their grades:
- Key: Student name (e.g., "Alice")
- Value: Grade (e.g., 85)

If hash table is used:
- The name "Alice" is passed to a hash function, which computes an index (say, 3).
- The grade 85 is stored at index 3 in the array.
- When searching for Alice’s grade, the hash function will return index 3, and the grade can be retrieved directly.

#### Basic Operations
1. <b>Insert, Update, Delete, Search</b>: Insert, Update, Delete and Search operations on Hash Table.
3. <b>Hash Functions</b>: Designing hash functions to distribute keys uniformly across the hash table.
4. <b>Rehashing</b>: Dynamically resizing the hash table when it becomes too full to maintain efficient operations.


### 1. Insert, Update, Delete, Search
In a hash table, the basic operations include insert (or update), delete, and search (or get).

#### Collision Handling
If two keys hash to the same index, need to resolve the collision using one of the following methods:
- Chaining: Store multiple key-value pairs in a linked list at the same index.
- Open Addressing: Probe for the next available slot if a collision occurs.


### 2. Hash Functions
Designing hash functions that distribute keys uniformly across a hash table is crucial to minimize collisions and maintain the efficiency of hash table operations. A good hash function should map keys to indices in a way that avoids clustering (where many keys are mapped to the same index) and spreads the keys as uniformly as possible across the table.

#### Common Strategies for Designing Hash Functions
1. <b>Division Method (Modulus Hashing)</b>: The hash value is computed by taking the remainder of the division of the key by the size of the hash table. Simple and effective when the table size is a prime number.
2. <b>Multiplication Method</b>: The key is multiplied by a constant fraction (usually a number between 0 and 1), and the fractional part is used to compute the hash value.
3. <b>Mid-Square Method</b>: The key is squared, and the middle digits of the result are taken as the hash value. This method works well for numeric keys and ensures more uniform distribution since it uses more bits of the key. Works well for numeric keys.
4. <b>Polynomial Hashing (for strings)</b>: For non-numeric keys, such as strings, a common method is to treat the characters in the string as digits of a large number in some base.
5. <b>Universal Hashing</b>: In universal hashing, a family of hash functions is selected randomly for each run of the program. This approach ensures that the probability of collision between any two keys is minimized, even in the worst-case scenario.


### 3. Rehashing
Dynamically resizing a hash table when it becomes too full is a key technique to maintain efficient operations such as insertions, deletions, and lookups. As the number of elements in the hash table grows, the likelihood of collisions increases, which degrades the performance of the hash table. Resizing the hash table helps to maintain low collision rates and ensures that the operations remain efficient.

#### Steps for Dynamically Resizing a Hash Table
1. <b>Set a Load Factor Threshold</b>: The load factor of a hash table is defined as the ratio of the number of elements (n) to the total number of available slots (m) in the table: <b>load factor = n / m</b>. When the load factor exceeds a predefined threshold (commonly 0.75), the hash table is resized to maintain performance.
2. <b>Create a Larger Hash Table</b>: When resizing, a new hash table with more slots is created. A common strategy is to double the size of the hash table, ensuring enough space to accommodate more elements and reduce collisions.
3. <b>Rehash All Existing Elements</b>: Each element in the original hash table must be rehashed and inserted into the new, larger hash table. The reason for rehashing is that the hash function uses the size of the table as part of its calculation, and changing the table size changes the indices where the elements are stored.
4. <b>Adjust the Threshold</b>: Once the table is resized, the threshold for the load factor is adjusted according to the new table size.