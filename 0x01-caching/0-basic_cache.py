#!/usr/bin/env python3

from base_caching import BaseCaching
"""
This is class will inherit from base caching class
"""


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

        for keys in self.cache_data.keys():
            if keys is key:
                return self.cache_data[keys]


