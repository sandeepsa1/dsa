def calculate_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        span[i] = i + 1 if not stack else i - stack[-1]

        stack.append(i)

    return span


prices = [100, 80, 60, 70, 60, 75, 85]
result = calculate_span(prices)
print(result)  # [1, 1, 1, 2, 1, 4, 6]