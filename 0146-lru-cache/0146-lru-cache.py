from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # This will maintain the order of keys.
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed item to the end to mark it as recently used.
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1  # Return -1 if the key doesn't exist.

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value of the existing key and move it to the end.
            self.cache.move_to_end(key)
        self.cache[key] = value

        # If the cache exceeds the capacity, remove the least recently used item (first item).
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
