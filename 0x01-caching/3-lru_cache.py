#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching
    and implements an LRU (Least Recently Used) caching strategy.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Store a key-value pair in the cache. If the number of items exceeds
        MAX_ITEMS, discard the least recently used item (LRU algorithm).

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.usage.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.
        If key is None or doesn't exist, return None.

        Args:
            key (str): The key to retrieve the item.

        Returns:
            any: The item stored in the cache, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None
