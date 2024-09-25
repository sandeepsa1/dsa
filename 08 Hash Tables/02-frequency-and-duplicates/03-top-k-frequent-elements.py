from collections import Counter

def top_k_frequent(arr, k):
    frequency = Counter(arr)
    
    sorted_elements = sorted(frequency, key=frequency.get, reverse=True)
    
    return sorted_elements[:k]


arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
k = 2

result = top_k_frequent(arr, k)

print(result)  # [3, 1]