class HashTable:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        self.table = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity
        self.load_factor_threshold = load_factor_threshold
    
    def hash_function(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor_threshold:
            self.resize()
        
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
            self.size += 1
        else:
            self.table[index] = (key, value)
    
    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        for item in self.table:
            if item is not None:
                key, value = item
                new_index = hash(key) % new_capacity
                new_table[new_index] = (key, value)
        self.table = new_table
        self.capacity = new_capacity
    
    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            return self.table[index][1]
        return None


hash_table = HashTable()
for i in range(10):
    hash_table.insert(i, i * 100)

print(hash_table.table)