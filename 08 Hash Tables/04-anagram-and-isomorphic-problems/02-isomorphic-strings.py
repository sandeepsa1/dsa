def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s, t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2
        
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
    
    return True


s = "egg"
t = "add"
print(isIsomorphic(s, t))  # True

s = "foo"
t = "bar"
print(isIsomorphic(s, t))  # False

s = "paper"
t = "title"
print(isIsomorphic(s, t))  # True