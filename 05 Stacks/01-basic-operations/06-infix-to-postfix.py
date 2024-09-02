precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

def infix_to_postfix(expression):
    stack = []
    output = []

    for token in expression:
        if token.isalnum():  # if the token is an operand (alphanumeric), add it to the output
            output.append(token)
        elif token == '(':  # if the token is '(', push it to the stack
            stack.append(token)
        elif token == ')':  # if the token is ')', pop until '(' is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # discard the '('
        else:  # if the token is an operator
            while (stack and stack[-1] != '(' and
                   (precedence[token] < precedence[stack[-1]] or
                    (precedence[token] == precedence[stack[-1]] and associativity[token] == 'L'))):
                output.append(stack.pop())
            stack.append(token)

    while stack: # Pop all the remaining operators from the stack
        output.append(stack.pop())

    return ''.join(output)


infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # abcd^e-fgh*+^*+i-
