#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''

        if key is None or item is None:
            return

        ln = len(self.cache_data)
        if (ln >= BaseCaching.MAX_ITEMS) and (key not in self.cache_data):
            for ky in self.cache_data.keys():
                first_key = ky
                self.cache_data.pop(ky)
                break
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        return self.cache_data.get(key, None)
