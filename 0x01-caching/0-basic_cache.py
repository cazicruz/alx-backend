#!/usr/bin/env python3
""" caching task """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ceching class that inherits from BaseCeching"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ a method to get the value to thr key passed"""
        if key in self.cache_data:
            return self.cache_data[key]
