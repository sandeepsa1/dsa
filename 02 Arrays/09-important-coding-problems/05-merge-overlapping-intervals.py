def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        last_interval = merged[-1]
        current_interval = intervals[i]
        
        if current_interval[0] <= last_interval[1]:
            merged[-1][1] = max(last_interval[1], current_interval[1])
        else:
            merged.append(current_interval)
    
    return merged

intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]] # Output: [[1, 6], [8, 10], [15, 18]]
# intervals2 = [[1, 4], [4, 5]] # Output: [[1, 5]]
print(merge_intervals(intervals1))