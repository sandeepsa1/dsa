def sort_stack(original_stack):
    auxiliary_stack = []

    while original_stack:
        temp = original_stack.pop()

        while auxiliary_stack and auxiliary_stack[-1] < temp:
            original_stack.append(auxiliary_stack.pop())

        auxiliary_stack.append(temp)

    while auxiliary_stack:
        original_stack.append(auxiliary_stack.pop())


stack = [34, 3, 31, 98, 92, 23]

print("Original Stack:", stack)
sort_stack(stack)
print("Sorted Stack:", stack)