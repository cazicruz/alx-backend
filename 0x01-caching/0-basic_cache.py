#!/usr/bin/env python3
""" caching task """
BaseCaching = __import__('base_caching.py').Basecaching


def class BasicCache(BaseCaching):
    """ceching class that inherits from BaseCeching"""
    def __init__(self):
        super.__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            break
        else:
            self.cache_data.update({key:item})

    def get(self, key):
        """ a method to get the value to thr key passed"""
        if key in self.cache_data:
            return self.cache_data.get(key)
