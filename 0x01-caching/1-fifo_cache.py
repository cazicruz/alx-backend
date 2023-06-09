#!/usr/bin/env python3
"""Basic caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out queue logic for cache"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstIn, _ = self.cache_data.popitem(False)
            print("DISCARD:", firstIn)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
