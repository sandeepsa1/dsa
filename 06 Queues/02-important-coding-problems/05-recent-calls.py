from collections import deque

def recent_calls(timestamps, time_frame):
    call_queue = deque()
    result = []

    for time in timestamps:
        call_queue.append(time)

        while call_queue and call_queue[0] < time - time_frame:
            call_queue.popleft()

        result.append(len(call_queue))
    
    return result


timestamps = [1, 100, 3001, 3002, 4000, 6000]
time_frame = 3000
print(recent_calls(timestamps, time_frame)) # [1, 2, 3, 3, 3, 4]