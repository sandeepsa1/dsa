def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and len(token) > 1):
            stack.append(int(token))
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            if token == '+':
                result = left_operand + right_operand
            elif token == '-':
                result = left_operand - right_operand
            elif token == '*':
                result = left_operand * right_operand
            elif token == '/':
                result = int(left_operand / right_operand)
            
            stack.append(result)
    
    return stack.pop()


tokens = ["2", "1", "+", "3", "*"]
result = eval_rpn(tokens)
print("Result:", result)  # 9