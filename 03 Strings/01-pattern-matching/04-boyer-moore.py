def bad_character_table(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0

    bad_char = bad_character_table(pattern)
    
    s = 0
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    
    return -1


text1 = "here is a simple example"
pattern1 = "example"
print(boyer_moore(text1, pattern1))