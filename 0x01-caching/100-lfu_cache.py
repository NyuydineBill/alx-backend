#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair

        Args:
            key: The key of the item
            item: The value to be cached
        """
        if key is None or item is None:
            return

        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == lfu]
            if len(lfu_keys) > 1:
                lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
                discard = min(lru_lfu, key=lru_lfu.get)
            else:
                discard = lfu_keys[0]

            print(f"DISCARD: {discard}")
            del self.cache_data[discard]
            del self.usage[self.usage.index(discard)]
            del self.frequency[discard]

        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        if key in self.usage:
            self.usage.remove(key)

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with a given key from the cache

        Args:
            key: The key to look up in the cache

        Returns:
            The value associated with the key if found, None otherwise
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None
