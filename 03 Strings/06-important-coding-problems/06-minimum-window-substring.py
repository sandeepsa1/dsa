from collections import Counter, defaultdict

def min_window(s, t):
    if not t or not s:
        return ""

    t_count = Counter(t)
    required = len(t_count)

    left, right = 0, 0
    formed = 0

    window_counts = defaultdict(int)

    min_len = float("inf")
    result = (0, 0)

    while right < len(s):
        char = s[right]
        window_counts[char] += 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)

            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1    

        right += 1    

    left, right = result
    return s[left:right + 1] if min_len != float("inf") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"