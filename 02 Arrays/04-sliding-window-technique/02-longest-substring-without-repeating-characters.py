def longest_substring_without_repeating_characters(s):
    char_set = set()
    max_length = 0
    start = 0
    max_start = 0  # To track starting index of the longest substring
    
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        char_set.add(s[end])
        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start
    
    return max_length, s[max_start:max_start + max_length]

s = "abcabcbb"
length, substring = longest_substring_without_repeating_characters(s)
print(f"The length of the longest substring without repeating characters is {length}.")
print(f"The longest substring without repeating characters is '{substring}'.")