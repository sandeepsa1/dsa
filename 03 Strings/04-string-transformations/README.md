## String Pattern Matching Algorithms
String transformation generally refers to the process of converting one string into another, converting string to integer or vice versa, changing case, etc.<br/>

Algorithms included here are;
1. <b>String to Integer (atoi)</b>: Converts a string to an integer.
2. <b>Integer to String (itoa)</b>: Converts an integer to a string.


### 1. String to Integer (atoi)
The "String to Integer (atoi)" problem involves implementing a function that converts a string to an integer, similar to the atoi function in C/C++. This function should handle various edge cases such as leading/trailing whitespace, optional signs, and invalid characters.</br>

1. Time complexity: <b>𝑂(n)</b>
2. Space complexity: <b>𝑂(1)</b></br>

#### Steps
1. Trim the string:
   - Remove leading and trailing whitespaces.
2. Check for an optional sign:
   - Determine if there is a '+' or '-' sign.
3. Convert the digits:
   - Parse the digits until a non-digit character is encountered.
4. Handle overflow:
   - Ensure the number is within the 32-bit signed integer range.


### 2. Integer to String (itoa)
The "Integer to String (itoa)" problem involves converting an integer to its corresponding string representation. This is essentially the reverse of the above atoi function.</br>

1. Time complexity: <b>𝑂(log n)</b>
2. Space complexity: <b>𝑂(log n)</b></br>

#### Steps
1. Handle the sign:
   - If the integer is negative, store the sign and work with the absolute value of the number.
2. Extract digits:
   - Extract digits from the integer by repeatedly dividing by 10 and collecting the remainder.
3. Build the string:
   - Convert each digit to its corresponding character and build the string in reverse order.
4. Add the sign back:
   - If the number was negative, add the sign back to the string.