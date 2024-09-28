## Anagram and Isomorphic Problems
Anagram and Isomorphic Problems using Hash Table.

Samples included are;
1. <b>Find All Anagrams in a String</b>: Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
2. <b>Isomorphic Strings</b>: Given two strings s and t, determine if they are isomorphic.
3. <b>Minimum Index Sum of Two Lists</b>: Given two lists of strings, find the common interest with the least list index sum.


### 1. Find All Anagrams in a String
To find all the start indices of anagrams of string p in string s, use a sliding window technique along with a hash map (or a frequency count array) to track the characters in the current window of s and compare it to the character frequency of p.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b>

#### Steps
1. Frequency map:
    - First, create a frequency count for string p.
2. Sliding window:
    - Slide over string s with a window of the same length as p. Adjust the frequency count as you move the window.
3. Comparison:
    - At each step, compare the frequency count of the current window with that of p. If they match, the window represents an anagram of p.


### 2. Isomorphic Strings
To determine if two strings s and t are isomorphic, check if each character in s can be mapped to a unique character in t such that all occurrences of a character in s map to the same character in t and vice versa.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b>

#### Steps
1. If the lengths of s and t are not the same, return False.
2. Use two dictionaries to store the mapping from s to t and from t to s.
3. For each character in s and t, check if the mapping is consistent:
    - If s[i] is already mapped to a character other than t[i], return False.
    - If t[i] is already mapped to a character other than s[i], return False.
4. If no conflicts arise, the strings are isomorphic.


### 3. Minimum Index Sum of Two Lists
Given two lists of strings representing two people's favorite interests (like restaurant names or hobbies). Find all the common interests between the two lists. Among these common interests, the goal is to find the one(s) where the sum of the indices in both lists is the smallest. If there is more than one interest with the smallest index sum, return all of them.

1. Time complexity: <b>𝑂(n + m)</b>
2. Space complexity: <b>𝑂(n)</b>

#### Steps
1. Use a dictionary to map each string in list1 to its index.
2. Traverse list2, and for each common string (found in both lists), calculate the index sum.
3. Keep track of the minimum index sum and collect the interests that have this minimum sum.
4. Return the list of common interests with the smallest index sum.