#!/usr/bin/env python3
"""Basic MRU caching module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """least recently used logic for cache"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.lru = {}
        self.tm = 0

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            """ then find the least entry"""
            old_key = max(self.lru.keys(), key = lambda k: self.lru[k])
            self.cache_data.pop(old_key)
            self.lru.pop(old_key)
            print("DISCARD:", old_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key in self.cache_data:
            self.lru[key] = self.tm
            self.tm = self.tm + 1
        return self.cache_data.get(key, None)
