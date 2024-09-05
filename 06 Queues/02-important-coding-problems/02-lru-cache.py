from collections import OrderedDict

def lru_cache(capacity):
    cache = OrderedDict()
    
    def get(key):
        if key not in cache:
            return -1
        else:
            cache.move_to_end(key, last=False)
            return cache[key]
    
    def put(key, value):
        if key in cache:
            cache.move_to_end(key, last=False)
            cache[key] = value
        else:
            if len(cache) >= capacity:
                cache.popitem(last=True)
            cache[key] = value
            cache.move_to_end(key, last=False)

    return get, put


capacity = 2
get, put = lru_cache(capacity)

put(1, 1)  # Cache: {1: 1}
put(2, 2)  # Cache: {1: 1, 2: 2}
print(get(1))  # Returns 1 and moves key 1 to the front -> Cache: {2: 2, 1: 1}
put(3, 3)  # Evicts key 2 and inserts key 3 -> Cache: {1: 1, 3: 3}
print(get(2))  # Returns -1 (not found)
put(4, 4)  # Evicts key 1 and inserts key 4 -> Cache: {3: 3, 4: 4}
print(get(1))  # Returns -1 (not found)
print(get(3))  # Returns 3 and moves key 3 to the front -> Cache: {4: 4, 3: 3}
print(get(4))  # Returns 4 and moves key 4 to the front -> Cache: {3: 3, 4: 4}