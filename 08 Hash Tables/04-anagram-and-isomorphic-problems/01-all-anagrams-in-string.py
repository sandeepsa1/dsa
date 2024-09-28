from collections import Counter

def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    
    result = []
    p_count = Counter(p)
    s_count = Counter()
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result


s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)  # [0, 6] (Anagrams start at indices 0 and 6)