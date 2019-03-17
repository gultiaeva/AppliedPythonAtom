#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        return True if key in self else default_value

    def put(self, key):
        super().put(key, None)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().keys()

    def intersect(self, another_hashset):
        res = HashSet()
        for item in another_hashset.values():
            if item in self:
                res.put(item)
        return res
