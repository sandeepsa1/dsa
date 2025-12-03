def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        # Track how far we can reach
        farthest = max(farthest, i + nums[i])
        
        # When we reach the end of the current "level"
        if i == current_end:
            jumps += 1          # We complete one BFS layer
            current_end = farthest  # Move to next layer
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps


nums = [2,3,1,1,4]
res = jump(nums)
print(res) # 2