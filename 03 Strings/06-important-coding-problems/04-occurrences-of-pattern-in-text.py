def calculate_z(S):
    Z = [0] * len(S)
    L, R, K = 0, 0, 0
    for i in range(1, len(S)):
        if i > R:
            L, R = i, i
            while R < len(S) and S[R] == S[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < len(S) and S[R] == S[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

def z_algorithm(pattern, text):
    combined = pattern + '$' + text
    Z = calculate_z(combined)
    pattern_length = len(pattern)
    matches = []

    for i in range(len(Z)):
        if Z[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches


text = "abxabcabcaby"
pattern = "abcaby"
print(z_algorithm(pattern, text))  # Output: [6]