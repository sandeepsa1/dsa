## Trie Based algorithms
Trie based algorithms are a class of algorithms that use a data structure called a Trie (pronounced "try") or prefix tree to efficiently store and retrieve strings, typically used for solving problems related to searching, prefix matching, and autocomplete functionalities.<br/>

A Trie is a tree-like data structure that stores a dynamic set of strings, where each node represents a single character of a string. The path from the root to a particular node represents a prefix of one or more strings in the Trie.<br/>

#### Key Characteristics of a Trie:
1. <b>Root Node</b>: The root node represents an empty string and does not store any character.
2. <b>Children Nodes</b>: Each node has multiple children, with each child node representing a character of the string.
3. <b>End Marker</b>: Nodes can have an end marker to indicate the end of a word (or string) stored in the Trie.
4. <b>Shared Prefixes</b>: Strings with common prefixes share the same path in the Trie up to the point where they differ.

Some codes implemented are;
1. <b>Trie Construction</b>: Builds a trie from a set of strings.
2. <b>Autocomplete</b>: Uses a trie to provide autocomplete suggestions.
3. <b>Longest Common Prefix</b>: Finds the longest common prefix among a set of strings.



### 1. Trie Construction
Constructing a Trie involves inserting words into a tree-like data structure where each node represents a character of the word. A step-by-step explanation of how to construct a Trie:

#### Trie Structure
1. <b>Node</b>: Each node in the Trie represents a single character.
2. <b>Children</b>: Each node can have multiple children, each representing the next character in the word.
3. <b>End of Word Marker</b>: A boolean flag (often isEndOfWord) is used to indicate if a node marks the end of a word.</br>

1. Time complexity: <b>Insertion: O(m) per word, O(n * m) for n words. Search: O(m) per word, O(n * m) for n words.</b>
2. Space complexity: <b>O(Σ * m * n)</b> to <b>O(m * n)</b></br>

#### Steps
1. Initialize the Root Node:
   - Start with an empty root node that represents the starting point of the Trie.
2. Insert Each Word:
   - For each word, start at the root node and insert each character as a child node. If a character node already exists, move to that node and continue with the next character.
3. Mark the End of the Word:
   - After inserting the last character of a word, mark the node as the end of a word by setting the 'isEndOfWord' flag.


### 2. Autocomplete
Given a list of words, implement an autocomplete system that, given a prefix, returns all words in the list that start with that prefix.</br>

1. Time complexity: <b>O(p + n)</b>
2. Space complexity: <b>O(p + n)</b></br>

#### Steps
1. Building the Trie:
   - First build the trie by inserting all the words into it.
2. Searching for a Prefix:
   -Ffind all words that start with a given prefix, then traverse the trie to the end of the prefix.
3. Collecting All Words with the Prefix:
   - Once the end of the prefix is reached, perform a depth-first search (DFS) from that node to collect all words that start with the prefix.
4. Autocomplete Function:
   - The autocomplete function combines the above steps.


### 3. Longest Common Prefix
Given a list of strings, find the longest common prefix among them. If there is no common prefix, return an empty string.</br>

1. Time complexity: <b>𝑂(n * m)</b>, where n is the number of strings and m is the length of the shortest string.
2. Space complexity: <b>𝑂(n * m)</b></br>

#### Steps
1. Define Trie Using Dictionaries:
   - Represent the trie using nested dictionaries, where each dictionary represents a node.
2. Insert Words into the Trie:
   - Insert all words into the Trie.
3. Find Longest Common Prefix:
   - Find the longest common prefix by traversing the trie.
4. Add the sign back:
   - If the number was negative, add the sign back to the string.