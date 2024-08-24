#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching
    and implements a FIFO caching strategy.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Store a key-value pair in the cache. If the number of items exceeds
        MAX_ITEMS, discard the first item put in the cache (FIFO algorithm).

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.
        If key is None or doesn't exist, return None.

        Args:
            key (str): The key to retrieve the item.

        Returns:
            any: The item stored in the cache, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
