#!/usr/bin/python3
"""This is a Cache kinda implementation of the Cache replacement policies
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class implements the FIFO replacement policy"""
    def __init__(self):
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.popitem()
        else:
            self.cache_data[key] = item
        # if key in self.cache_data:
        #     self.keys_order.remove(key)
        # elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        #     last_key = len(self.keys_order) - 1
        #     del self.cache_data[last_key]
        #     print(f"DISCARD: {last_key}")
        #
        # self.cache_data[key] = item
        # self.keys_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
