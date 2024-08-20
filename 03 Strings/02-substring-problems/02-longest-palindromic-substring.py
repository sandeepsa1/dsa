def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes (single character center)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even-length palindromes (two-character center)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest


s = "cacad"
result = longest_palindromic_substring(s)
print(f"The longest palindromic substring is: '{result}'")