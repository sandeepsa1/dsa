def count_and_say(n):
    if n == 1:
        return "1"

    # Start with the first term
    current_term = "1"

    # Generate the sequence up to the n-th term
    for i in range(2, n + 1):
        next_term = ""
        count = 1

        # Iterate over the current term to build the next term
        for j in range(1, len(current_term)):
            if current_term[j] == current_term[j - 1]:
                count += 1
            else:
                next_term += str(count) + current_term[j - 1]
                count = 1

        # Add the last counted group
        next_term += str(count) + current_term[-1]
        
        # Update current_term to the newly generated next_term
        current_term = next_term

    return current_term


print(count_and_say(1))  # Output: "1"
print(count_and_say(4))  # Output: "1211"
print(count_and_say(5))  # Output: "111221"
print(count_and_say(6))  # Output: "312211"