def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    return None

def is_empty(stack):
    return len(stack) == 0


stack = []

push(stack, 1)
push(stack, 2)
push(stack, 3)

print(peek(stack))  # 3
print(pop(stack))   # 3
print(pop(stack))   # 2
print(is_empty(stack))  # False
print(pop(stack))   # 1
print(is_empty(stack))  # True