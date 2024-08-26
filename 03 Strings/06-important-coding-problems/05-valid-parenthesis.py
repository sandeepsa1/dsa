def is_valid_parentheses(s):
    matching_bracket = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False
        else:
            return False

    return not stack


print(is_valid_parentheses("()"))       # Output: True
print(is_valid_parentheses("()[]{}"))   # Output: True
print(is_valid_parentheses("(]"))       # Output: False
print(is_valid_parentheses("([)]"))     # Output: False
print(is_valid_parentheses("{[]}"))     # Output: True