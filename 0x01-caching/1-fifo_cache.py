#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order_of_entrance = []


    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > Base.Caching.MAX_ITEMS:
            for k in self.cache_data:
                if k == self.order_of_entrance[0]:
                    self.cache_data.pop(k)
                    self.order_of_entrance.pop(0)
                    print("discard:",k)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
