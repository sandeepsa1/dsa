# Given:
#   A start word
#   A target word
#   A dictionary (word list)
# Change only one letter at a time, and each intermediate word must exist in the dictionary.
from collections import deque

def word_ladder_length(start, end, wordList):
    word_set = set(wordList)
    if end not in word_set:
        return 0 

    queue = deque([(start, 1)])
    visited = set([start])

    while queue:
        word, length = queue.popleft()
        if word == end:
            return length

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    return 0


start = "hit"
end = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print("Shortest transformation length:", word_ladder_length(start, end, wordList))