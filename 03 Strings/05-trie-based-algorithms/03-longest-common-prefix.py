def insert_word(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['*'] = True

def longest_common_prefix_trie(strs):
    if not strs:
        return ""

    trie = {}
    for word in strs:
        insert_word(trie, word)

    prefix = []
    node = trie
    while node:
        # If the node has more than one child or marks the end of a word, stop
        if len(node) != 1 or '*' in node:
            break

        # Get the single character and move to the next node
        char = next(iter(node))
        prefix.append(char)
        node = node[char]

    return ''.join(prefix)


print(longest_common_prefix_trie(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix_trie(["dog", "racecar", "car"]))     # Output: ""
print(longest_common_prefix_trie(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(longest_common_prefix_trie(["throne", "throne"]))          # Output: "throne"
print(longest_common_prefix_trie(["apple", "ape", "april"]))     # Output: "ap"