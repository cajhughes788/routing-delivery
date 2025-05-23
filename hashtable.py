# This is a basic Hash Table class that stores items using key-value pairs
class HashTable:
    def __init__(self, size=40):
        # Create a list with empty lists for each bucket (chaining to handle collisions)
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Simple hash function using modulo to find index
        return int(key) % self.size

    def insert(self, key, item):
        # Insert a key-item pair into the hash table
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists in this bucket; if so, update value
        for entry in bucket:
            if entry[0] == key:
                entry[1] = item
                return

        # Otherwise, append the new key-item pair
        bucket.append([key, item])

    def lookup(self, key):
        # Return the item associated with the given key
        index = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry[0] == key:
                return entry[1]

        # Return None if the key is not found
        return None

