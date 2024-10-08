def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    
    return -1


s = "testcode"
result = first_non_repeating_char(s)
print(result)  # 2 (since 's' is the first non-repeating character)