#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching
    and implements a basic caching strategy with no limit.

    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair in the cache. If key or item is None, do nothing.

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
