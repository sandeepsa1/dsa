## Stacks
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle, meaning the last element added to the stack will be the first one to be removed. Stacks are used in various applications, including expression evaluation, backtracking algorithms, undo mechanisms in text editors, and more.

#### Algorithms included here are;
1. <b>Push, Pop, Peek, IsEmpty</b>: Basic Stack operations
2. <b>Sort a Stack</b>: Sort the elements in a stack using another stack.
3. <b>Reverse a String</b>: Reverse the characters in a string using a stack.
4. <b>Evaluate Reverse Polish Notation</b>: Description: Evaluate the value of an arithmetic expression in Reverse Polish Notation.
5. <b>Min Stack</b>: Design a stack that supports push, pop, and retrieving the minimum element in constant time.
6. <b>Infix to Postfix Conversion</b>: Convert an infix expression (e.g., a + b) to a postfix expression (e.g., ab+).
7. <b>Evaluate Postfix Expression</b>: Evaluate a postfix expression to get the result.



### 1. Push, Pop, Peek, IsEmpty
push, pop, peek, and isEmpty are the basic operations that can be performed on a stack.


### 2. Sort a Stack
Sorting a stack using another stack is a classic problem that demonstrates the effective use of auxiliary data structures to manipulate data. The goal is to rearrange the elements in the original stack such that they are sorted in ascending or descending order, using only one additional stack for temporary storage.

1. Time complexity: <b>𝑂(n<sup>2</sup>)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Initialize an auxiliary stack.
2. Pop elements from the original stack one by one.
3. For each popped element, compare it with the top of the auxiliary stack:
   - If the auxiliary stack is empty or the top element of the auxiliary stack is smaller than the current element, push the element onto the auxiliary stack.
   - If the top element of the auxiliary stack is larger than the current element, pop from the auxiliary stack and push the popped element back to the original stack until the correct position is found for the current element.
4. Repeat until the original stack is empty.
5. The auxiliary stack will now be sorted in ascending order.


### 3. Reverse a String
Reversing the characters in a string using a stack can be done by pushing each character of the string onto the stack and then popping them one by one to form the reversed string. This leverages the LIFO (Last In, First Out) property of stacks.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Initialize an empty stack:
   - Create an empty stack to store the characters of the string.
2. Push all characters of the string onto the stack:
   - Loop through each character in the string.
   - For each character, push it onto the stack.
3. Pop all characters from the stack to form the reversed string:
   - Initialize an empty string called 'reversed_string'.
   - While the stack is not empty, pop the top character from the stack and append it to 'reversed_string'.
4. Return the reversed string:
   - Once the stack is empty, 'reversed_string' will contain the characters in reverse order. Return this string.


### 4. Evaluate Reverse Polish Notation
Evaluating an arithmetic expression in Reverse Polish Notation can be done by processing each element of the expression from left to right. When an operand is encountered, it is pushed onto a stack. When an operator is encountered, the necessary number of operands (usually two) are popped from the stack, the operation is performed, and the result is pushed back onto the stack. The final value on the stack is the result of the expression.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(N)</b></br>

#### Steps
1. Initialize an empty stack:
   - Create an empty stack to store operands.
2. Iterate through each token in the expression:
   - If the token is an operand (i.e., a number), push it onto the stack.
   - If the token is an operator (e.g., '+', '-', '*', '/'):
      - Pop the top two operands from the stack.
      - Apply the operator to these operands in the correct order.
      - Push the result back onto the stack.
Final Result:
   - After processing all tokens, the stack will contain exactly one element, which is the result of the expression. Return this result.


### 5. Min Stack
Designing a stack that supports 'push', 'pop', and retrieving the 'minimum' element in constant time requires an auxiliary stack to keep track of the minimum elements.

1. Time complexity: <b>𝑂(1)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Push Operation:
   - Push the element onto the main stack.
   - If the min stack is empty or the element is smaller than or equal to the current minimum, push it onto the min stack.
2. Pop Operation:
   - Pop the element from the main stack.
   - If the popped element is the same as the top of the min stack, pop it from the min stack as well.
3. Get Min Operation:
   - Return the top element of the min stack, which is the current minimum.


### 6. Infix to Postfix Conversion
To convert an infix expression (like a + b) to a postfix expression (like ab+), use the Shunting Yard Algorithm developed by Edsger Dijkstra. This algorithm uses a stack to hold operators and ensures that the operators are applied in the correct order.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Initialize an empty stack for operators and an empty list for the output (postfix expression).
2. Read each token (operand, operator, or parenthesis) in the infix expression from left to right.
   - Operand: Directly add it to the output list.
   - Left Parenthesis ((): Push it onto the stack.
   - Right Parenthesis ()): Pop operators from the stack to the output list until a left parenthesis is encountered. Discard the left parenthesis.
   - Operator: Pop operators from the stack to the output list as long as the operator at the top of the stack has greater precedence or the same precedence (for left-associative operators). Then, push the current operator onto the stack.
3. Pop any remaining operators from the stack to the output list.
4. Return the output list as the postfix expression.


### 7. Evaluate Postfix Expression
To evaluate a postfix expression (also known as Reverse Polish Notation), you can use a stack-based approach. The idea is to process the postfix expression from left to right, using a stack to keep track of operands and applying operators as they appear.

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(n)</b></br>

#### Steps
1. Initialize an empty stack.
2. Read each token (operand or operator) in the postfix expression from left to right:
   - Operand: Push it onto the stack.
   - Operator: Pop the required number of operands from the stack (two for binary operators), apply the operator, and push the result back onto the stack.
3. The final value in the stack will be the result of the postfix expression.