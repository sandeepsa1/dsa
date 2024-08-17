def find_three_sum(arry, target):
    arry.sort()
    n = len(arry)

    for i in range(n - 2):
        if(i > 0 and arry[i] == arry[i - 1]): # Avoid duplicates
            continue

        left, right = i + 1, n - 1
        while left < right:
            current_sum = arry[i] + arry[left] + arry[right]

            if current_sum == target:
                return arry[i], arry[left], arry[right]
            elif current_sum < target: # Move left to increase sum since arry is sorted
                left += 1
            else:
                right -= 1

    return None

arry = [2, 7, 15, 19, 11]
target = 24
result = find_three_sum(arry, target)
if result:
    print(f"Three numbers that sum up to {target} are: {result}")
else:
    print("No three numbers found that sum up to the target.")