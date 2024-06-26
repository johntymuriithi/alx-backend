#!/usr/bin/env python3
"""
This is class will inherit from base caching class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        method to set the key item in the dict
        """
        if key and item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        method to get the item per key
        """
        if key is None:
            return
        return self.cache_data[key]
