class HashTable:
    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = [None] * table_size

    def string_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.table_size

    def insert(self, key, value):
        index = self.string_hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.string_hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.string_hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
        return False


hash_table = HashTable(table_size=10)
hash_table.insert("apple", 50)
hash_table.insert("banana", 100)

print(hash_table.get("apple"))   # 50
print(hash_table.get("banana"))  # 100

hash_table.delete("apple")
print(hash_table.get("apple"))   # None