def insert_into_trie(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True  # '#' is used to mark the end of a word

def print_trie(trie, level=0):
    for char, sub_trie in trie.items():
        if char == '#':
            print(' ' * level + "- End of Word")
        else:
            print(' ' * level + "- " + char)
            print_trie(sub_trie, level + 2)


trie = {}
words = ["cat", "car", "cart", "dog", "dot"]
for word in words:
    insert_into_trie(trie, word)

print("Trie Structure:")
print_trie(trie)