def itoa(num: int) -> str:
    if num == 0:
        return "0"

    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    result = []
    while num > 0:
        digit = num % 10
        result.append(chr(digit + ord('0')))
        num //= 10

    if is_negative:
        result.append('-')

    result.reverse()
    return ''.join(result)


print(itoa(123))
print(itoa(-456))
print(itoa(0))
print(itoa(789))