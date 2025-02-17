### Dictionary Operations
1. <b>Insert, Update, Delete, Check</b>: Insert, Update, Delete and Check operations on Dictionaries.
2. <b>Fetch Values and Iterations</b>: Fetch and Iteration operations on Dictionaries.
3. <b>Merge Dictionaries</b>: Combine two dictionaries into one, with values from the second dictionary overwriting those in the first.
4. <b>Default and Ordered Dictionaries</b>: Default and Ordered Dictionaries uses and differences.


#### 1. Insert, Update, Delete, Check
In a dictionary, the basic operations include Insert, Update, Delete and Check.

#### 2. Fetch Values and Iterations
Get Value by Key, Iterate over keys, Iterate over values and Iterate over key-value pairs.

#### 3. Merge Dictionaries
If the same key exists in both, the value from the second dictionary overwrites the value in the first. Three methods are possible.

#### 4. Default and Ordered Dictionaries
A defaultdict is a subclass of Python’s built-in dict that provides a default value for missing keys. This avoids KeyError when accessing non-existent keys.
An OrderedDict is a dictionary subclass that maintains the insertion order of keys. Note that from Python 3.7+, normal dictionaries also preserve order, but OrderedDict provides additional methods like move_to_end(). 