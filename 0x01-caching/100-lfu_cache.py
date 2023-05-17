#!/usr/bin/env python3
"""Basic caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """least recently used logic for cache"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.lfu = {}

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            """ then find the least entry"""
            old_key = min(self.lfu.keys(), key = lambda k: self.lfu[k])
            self.cache_data.pop(old_key)
            self.lfu.pop(old_key)
            print("DISCARD:", old_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key in self.cache_data:
            if key in self.lru:
                self.lfu[key] +=1
            else:
                self.lfu[key] = 0
        return self.cache_data.get(key, None)
