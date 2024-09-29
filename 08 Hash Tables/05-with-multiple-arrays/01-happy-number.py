def isHappy(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum
    
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


print(isHappy(19))  # True (19 is a happy number)
print(isHappy(2))   #  False (2 is not a happy number)