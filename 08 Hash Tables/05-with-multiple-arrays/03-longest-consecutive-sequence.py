def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


arr = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(arr))  # 4 (The longest sequence is [1, 2, 3, 4])

arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(arr))  # 9 (The longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8])