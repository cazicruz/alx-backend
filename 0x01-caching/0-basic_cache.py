#!/usr/bin/env python3
""" caching task """
from typing import Dict, Any
from base_caching import BaseCaching


def class BasicCache(BaseCaching):
    """ceching class that inherits from BaseCeching"""
    def __init__(self):
        super.__init__()

    def put(self, key: str, item: Any):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key: str) -> Dict:
        """ a method to get the value to thr key passed"""
        if key in self.cache_data:
            return self.cache_data[key]
