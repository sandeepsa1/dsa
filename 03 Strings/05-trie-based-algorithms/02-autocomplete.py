def insert_word(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['*'] = True  # Mark the end of a word

def search_prefix(trie, prefix):
    node = trie
    for char in prefix:
        if char not in node:
            return None
        node = node[char]
    return node

def collect_words(node, prefix, results):
    if '*' in node:
        results.append(prefix)
    for char in node:
        if char != '*':
            collect_words(node[char], prefix + char, results)

def autocomplete(trie, prefix):
    results = []
    node = search_prefix(trie, prefix)
    if node:
        collect_words(node, prefix, results)
    return results


trie = {}
words = ["apple", "app", "apex", "bat", "ball", "bark"]
for word in words:
    insert_word(trie, word)

print(autocomplete(trie, "ap"))
print(autocomplete(trie, "ba"))
print(autocomplete(trie, "cat"))
