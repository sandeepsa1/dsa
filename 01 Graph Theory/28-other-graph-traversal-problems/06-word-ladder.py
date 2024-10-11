from collections import deque, defaultdict

def word_ladder_length(start: str, end: str, word_list: list[str]) -> int:
    if end not in word_list:
        return 0

    word_len = len(start)

    all_combo_dict = defaultdict(list)

    for word in word_list:
        for i in range(word_len):
            pattern = word[:i] + "*" + word[i+1:]
            all_combo_dict[pattern].append(word)

    queue = deque([(start, 1)])
    
    visited = set()
    visited.add(start)

    while queue:
        current_word, level = queue.popleft()

        for i in range(word_len):
            pattern = current_word[:i] + "*" + current_word[i+1:]

            for neighbor in all_combo_dict[pattern]:
                if neighbor == end:
                    return level + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

            all_combo_dict[pattern] = []

    return 0


start_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

result = word_ladder_length(start_word, end_word, word_list)
print(f"The length of the shortest transformation sequence is: {result}") # 5 "hit" -> "hot" -> "dot" -> "dog" -> "cog"