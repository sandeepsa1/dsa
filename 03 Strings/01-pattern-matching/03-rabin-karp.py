def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    base = 256  # A base value for the hash function (typically the number of characters in the input alphabet)
    prime = 101  # A prime number used to mod the hash values to reduce collisions
    
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * base) % prime
    
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i
        
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            if text_hash < 0:
                text_hash += prime
    
    return -1


text1 = "abracadabra"
pattern1 = "cad"
print(rabin_karp(text1, pattern1))