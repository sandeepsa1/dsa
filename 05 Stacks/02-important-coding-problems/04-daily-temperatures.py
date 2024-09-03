def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day

        stack.append(i)

    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = daily_temperatures(temperatures)
print(result)  # [1, 1, 4, 2, 1, 1, 0, 0]