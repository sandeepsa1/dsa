main_stack = []
min_stack = []

def push(x):
    main_stack.append(x)
    if not min_stack or x <= min_stack[-1]:
        min_stack.append(x)

def pop():
    if main_stack:
        popped = main_stack.pop()
        if popped == min_stack[-1]:
            min_stack.pop()

def top():
    if main_stack:
        return main_stack[-1]
    return None

def get_min():
    if min_stack:
        return min_stack[-1]
    return None


push(2)
push(0)
push(3)
push(0)
print(get_min())  # 0
pop()
print(get_min())  # 0
pop()
print(get_min())  # 0
pop()
print(get_min())  # 2