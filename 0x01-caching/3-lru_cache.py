#!/usr/bin/python3
"""This is a Cache kinda implementation of the Cache replacement policies
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, remove it to update its position
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, remove the first (oldest) item
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

        # Add the key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
