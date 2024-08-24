## Important Coding Problems in Strings
Some of the important and most common coding problems related to Strings.<br/>

Some codes implemented are;
1. <b>Anagram Check</b>: Checks if two strings are anagrams of each other.
2. <b>Group Anagrams</b>: Groups a list of strings into anagrams.
3. <b>Count and Say</b>: Generates the n-th term in the count-and-say sequence.
4. <b>Z-Algorithm</b>: Finds occurrences of a pattern in a text using Z-values.


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