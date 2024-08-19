## String Pattern Matching Algorithms
String pattern matching algorithms are techniques used to find occurrences of a "pattern" (a sequence of characters) within a "text" (another sequence of characters). These algorithms are fundamental in various applications, including text editors, search engines, DNA sequencing, and more.<br/>

Algorithms included here are;
1. <b>Naive Pattern Matching</b>: Simple method to check if a pattern exists in a string.
2. <b>Knuth-Morris-Pratt (KMP)</b>: Efficiently searches for occurrences of a "word" within a "text".
3. <b>Rabin-Karp</b>: Uses hashing to find any one of a set of pattern strings in a text.
4. <b>Boyer-Moore</b>: Skips sections of the text to improve efficiency.

<b>Out of these, Boyer-Moore is the most efficient and widely used string-matching algorithm in practice, especially when dealing with large texts and relatively small patterns.</b>


### 1. Naive Pattern Matching
Naive pattern matching is the simplest method to check if a pattern exists in a string. The idea is to slide the pattern over the text one character at a time and check for a match at each position.</br>

1. Time complexity: <b>𝑂((n - m + 1) * m)</b> where 'n' is the length of the text and 'm' is the length of the pattern.
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Loop through the Text: Slide the pattern 'P' over the text 'T' from the beginning to the end, stopping when there are not enough characters left in 'T' to match 'P'.
2. Check for Match: For each position in the text where the pattern could start, compare the substring of 'T' with 'P'. If they match, return the starting index.
3. Return -1: If the pattern is not found after checking all possible positions, return '-1'.


### 2. Knuth-Morris-Pratt (KMP)
The Knuth-Morris-Pratt (KMP) algorithm is an efficient method for searching for occurrences of a "word" (pattern) within a "text". The key idea behind KMP is to avoid unnecessary comparisons by preprocessing the pattern to build a partial match table (also known as the "longest prefix suffix" or LPS array). This allows the algorithm to skip over portions of the text that have already been matched, thus reducing the overall time complexity.</br>

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(m)</b></br>

#### Steps
1. Build the LPS Array:
   - The LPS array is built by iterating through the pattern and finding the length of the longest proper prefix which is also a suffix for each prefix of the pattern.
   - If there’s a mismatch after 'j' matches, use 'LPS[j-1]' to determine the next positions to compare.
2. Search the Text Using the LPS Array:
   - Use the LPS array to determine how much to shift the pattern when a mismatch occurs.
   - If a match is found, return the starting index. If no match is found after processing the entire text, return '-1'.


### 3. Rabin-Karp
The Rabin-Karp algorithm is another string-searching algorithm, particularly effective for finding patterns in large texts. It uses hashing to find any one of a set of pattern strings in a text. The algorithm is known for its simplicity and efficiency in practice, especially when searching for multiple patterns.</br>

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Hash the Pattern:
   - Compute the hash value of the pattern.
2. Hash the Substrings:
   - Compute the hash value of the first substring of the text that is the same length as the pattern.
3. Compare Hashes:
   - Slide the pattern over the text one character at a time, recomputing the hash value of the new substring, and compare it with the hash value of the pattern.
      - If the hash values match, check the actual substring to confirm it's a match.
      - If the hashes don't match, continue to the next substring.
4. Return the Result:
   - If a match is found, return the starting index; otherwise, return '-1'.


### 4. Boyer-Moore
The Boyer-Moore algorithm is an efficient string-searching algorithm that is particularly effective when the pattern is much shorter than the text. It pre-processes the pattern and uses that information to skip sections of the text, making it faster than some other algorithms in many cases.</br>

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Preprocessing:
   - <b>Bad Character Table</b>: This table is built to determine the last occurrence of each character in the pattern. If a mismatch occurs, the pattern is shifted so that this last occurrence aligns with the mismatched character in the text.
   - <b>Good Suffix Table</b>: This table helps to determine how far to shift the pattern when a mismatch occurs after a partial match.
2. Searching the Text:
   - Start by aligning the pattern with the beginning of the text.
   - Compare characters of the pattern to the text from right to left.
   - If all characters match, return the starting index.
   - If a mismatch occurs, use the bad character and good suffix heuristics to determine how far to shift the pattern.
   - Repeat the process until the pattern is found or the end of the text is reached.


### When to Use Each:
1. <b>Boyer-Moore</b>: Best for general-purpose string searching, especially in large texts.
2. <b>KMP</b>: Useful when the pattern has repetitive structures or when you need to preprocess the pattern.
3. <b>Rabin-Karp</b>: Best for searching multiple patterns or when you need a rolling hash for other purposes.
4. <b>Naive Approach</b>: Useful for small problems where simplicity is more important than efficiency.