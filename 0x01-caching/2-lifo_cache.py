#!/usr/bin/python3
"""This is a Cache kinda implementation of the Cache replacement policies
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class implements the LIFO replacement policy"""
    def __init__(self):
        super().__init__()
        self.last = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last:
                print(f"DISCARD: {self.last}")
                del self.cache_data[self.last]

        self.cache_data[key] = item
        self.last = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
