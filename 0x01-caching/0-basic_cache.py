#!/usr/bin/env python3
""" caching task """


def class BasicCache(BaseCaching):
    """ceching class that inherits from BaseCeching"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            breake

        self.cache_data[key] = item
    def get(self, key):
        return self.cache_data.get(key)
