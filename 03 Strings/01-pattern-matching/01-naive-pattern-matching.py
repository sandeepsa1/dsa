def naive_pattern_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        if match:
            return i
    
    return -1


text1 = "hello"
pattern1 = "ll"
print(naive_pattern_matching(text1, pattern1))