## Important Coding Problems in Strings
Some of the important and most common coding problems related to Strings.<br/>

Some codes implemented are;
1. <b>Anagram Check</b>: Checks if two strings are anagrams of each other.
2. <b>Group Anagrams</b>: Groups a list of strings into anagrams.
3. <b>Count and Say</b>: Generates the n-th term in the count-and-say sequence.
4. <b>Z-Algorithm</b>: Finds occurrences of a pattern in a text using Z-values.
5. <b>Valid Parentheses</b>: Determine if a string containing just the characters '(', ')', '{', '}', '[' and ']', is valid.
6. <b>Minimum Window Substring</b>: Given a string S and a string T, find the minimum window in S which will contain all the characters in T.
7. <b>Zigzag Conversion</b>: Convert a string to a zigzag pattern on a given number of rows.


### 1. Anagram Check
The implemented method counts the frequency of each character in both strings and then compares the counts.


### 2. Group Anagrams
Various approaches possible. One method is to sort each word and the sorted word is used as the key in the dictionary. Anagrams will have the same sorted form and thus be grouped together.


### 3. Count and Say
The "Count and Say" sequence is a sequence of numbers where each term is generated based on the previous term. The sequence starts with "1", and each subsequent term describes the digits in the previous term.

#### Steps
1. Start with the string "1" as the first term.
2. For each subsequent term, read the previous term and describe it by counting consecutive digits and saying the count followed by the digit.
3. Continue this process until the n-th term is generated.


### 4. Z-Algorithm
The Z-Algorithm is an efficient string matching algorithm that finds all occurrences of a pattern in a text by using Z-values. The Z-values for a string represent the lengths of the longest substrings starting from each position in the string that are also prefixes of the string.

#### Steps
1. Concatenate the Pattern and Text:
   - Create a new string by concatenating the pattern 'P', a special character (e.g., '$'), and the text 'T'. This helps in calculating the Z-values.
2. Compute the Z-Array:
   - Compute the Z-array for this concatenated string. The Z-values for indices corresponding to the text 'T' will indicate where the pattern 'P' matches.
3. Find Matches:
   - If the Z-value at any index is equal to the length of the pattern 'P', it indicates the start of a match of the pattern in the text.


### 5. Valid Parentheses
To determine if a string containing only the characters '(', ')', '{', '}', '[', and ']' is valid, it is required to check if the parentheses are properly balanced and correctly nested.

#### Steps
1. Traverse the string from left to right.
2. Push each opening bracket onto the stack.
3. For each closing bracket, check if the stack is not empty and the top of the stack is the corresponding opening bracket.
4. If it is, pop the stack. If it’s not, or the stack is empty when a closing bracket is encountered, the string is invalid.
5. After processing the entire string, if the stack is empty, the string is valid; otherwise, it's invalid.


### 6. Minimum Window Substring
Given two strings 'S' and 'T', you need to find the minimum window in ''S' which contains all the characters of 'T', including duplicates. If there is no such window, return an empty string.

#### Steps
1. Frequency Count:
   - First, create a frequency count of characters in 'T'. This will help in keeping track of what characters and how many of them we need in the current window of 'S'.
2. Sliding Window:
   - Use two pointers ('left' and 'right') to create a sliding window in 'S'.
   - Expand the window by moving the 'right' pointer to the right.
   - Once the window contains all characters from 'T' (including their frequencies), try to minimize the window by moving the 'left' pointer to the right.
3. Updating the Result:
   - Keep track of the minimum window size that satisfies the condition.
   - If a smaller window is found, update the result.
4. Edge Cases:
   - If 'T' is longer than 'S', return an empty string.
   - If 'T' is empty, return an empty string.
   - If 'S' does not contain all characters of 'T', return an empty string.


### 7. Zigzag Conversion
The "Zigzag Conversion" problem involves rearranging a given string in a zigzag pattern over a specified number of rows and then reading the pattern row by row to form a new string.

#### Steps
1. Handle Edge Cases:
   - If 'numRows' is 1, the zigzag pattern is just the original string.
   - If 'numRows' is greater than or equal to the length of the string, return the string itself since each character will be on a new line.
1. Simulate Zigzag Traversal:
   - Use a list of strings (one for each row) to store characters.
   - Traverse the string, appending characters to the appropriate row.
   - Change the direction (up or down) when you reach the top or bottom row.
1. Combine Rows:
   - After filling the rows according to the zigzag pattern, combine all the rows to form the final string.