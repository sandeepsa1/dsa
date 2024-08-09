def find_k_sum(arry, target, k):
    def k_sum_recursive(start, target, k, path):
        if k == 1:
            if target in arry[start:]:
                results.append(path + [target])
            return
        else:
            for i in range(start, len(arry) - k + 1):
                if i > start and arry[i] == arry[i - 1]: # No need to consider duplicate items
                    continue
                k_sum_recursive(i + 1, target - arry[i], k - 1, path + [arry[i]])

    arry = sorted(arry)
    results = []
    k_sum_recursive(0, target, k, [])
    
    return results

arry = [2, 7, 15, 19, 11, 14, 5, 1]
target = 20
k = 3
result = find_k_sum(arry, target, k)
if result:
    for res in result:
        print(f"Numbers that sum up to {target} are: {res}")
else:
    print(f"No combination of {k} numbers found that sum up to the target.")