def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            elif token == '^':
                stack.append(a ** b)
    
    return stack[0] if stack else None


postfix_expression = "231*+9-"
result = evaluate_postfix(postfix_expression)
print(result)  # -4