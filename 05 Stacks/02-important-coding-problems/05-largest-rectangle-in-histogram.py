def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            height = heights[top_of_stack]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)

    while stack:
        top_of_stack = stack.pop()
        height = heights[top_of_stack]
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
result = largest_rectangle_area(heights)
print(result)  # 10