def atoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    i, n = 0, len(s)
    # Step 1: Ignore leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Check for optional sign
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Step 3: Convert digits to integer
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        # Step 4: Handle overflow and underflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1

    return sign * result


s = "42"
print(atoi(s))  # Output: 42

s = "   -42"
print(atoi(s))  # Output: -42

s = "4193 with words"
print(atoi(s))  # Output: 4193

s = "words and 987"
print(atoi(s))  # Output: 0

s = "-91283472332"
print(atoi(s))  # Output: -2147483648 (clamped)