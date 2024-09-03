def next_greater_elements(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            nge[i] = stack[-1]
        
        stack.append(arr[i])

    return nge


arr = [4, 5, 2, 10, 8]
result = next_greater_elements(arr)
print(result)  # [5, 10, 10, -1, -1]