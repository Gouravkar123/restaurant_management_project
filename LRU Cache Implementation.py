class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}      # stores key-value pairs
        self.usage = []      # maintains access order (most recent at the end)

    def get(self, key: int) -> int:
        if key not in self.cache:
            print(f"Get {key}: -1 (Not Found)")
            return -1

        # Update usage (move key to the end -> most recently used)
        self.usage.remove(key)
        self.usage.append(key)
        print(f"Get {key}: {self.cache[key]}")
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.append(key)
            print(f"Updated {key} -> {value}")
        else:
            # Evict if full
            if len(self.cache) >= self.capacity:
                lru_key = self.usage.pop(0)  # remove least recently used
                del self.cache[lru_key]
                print(f"Evicted {lru_key} (LRU)")

            # Insert new key
            self.cache[key] = value
            self.usage.append(key)
            print(f"Inserted {key} -> {value}")

    def display(self):
        print("Cache State:", {k: self.cache[k] for k in self.usage})
