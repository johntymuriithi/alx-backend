#!/usr/bin/python3

from base_caching import BaseCaching
"""
This is class will inherit from base caching class
"""


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return

        for keys in self.cache_data.keys():
            if keys is key:
                return self.cache_data[keys]


