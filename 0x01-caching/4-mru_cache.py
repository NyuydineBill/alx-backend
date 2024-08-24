#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Cache a key-value pair

        Args:
            key: The key of the item
            item: The value to be cached
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.usage.pop()
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

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
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None
