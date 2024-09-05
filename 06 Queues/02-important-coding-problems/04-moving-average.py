from collections import deque

def moving_average(stream, k):
    window = deque()
    window_sum = 0
    result = []
    
    for num in stream:
        # Step 1: Add the new number to the window
        window.append(num)
        window_sum += num

        # Step 2: If window size exceeds k, remove the oldest element
        if len(window) > k:
            oldest = window.popleft()
            window_sum -= oldest

        # Step 3: Calculate the average and store it in the result list
        result.append(window_sum / len(window))
    
    return result


stream = [1, 3, 5, 7, 9, 11]
window_size = 3
print(moving_average(stream, window_size)) # [1.0, 2.0, 3.0, 5.0, 7.0, 9.0]