#!/usr/bin/env python
# coding: utf-8
from collections import deque
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        self.maxsize = maxsize
        self.ttl = ttl
        self.queue = deque()
        self.timestamp = time.time()

    def __call__(self, function):
        def wrapped(*args, **kwargs):
            if self.ttl and time.time() - self.timestamp > self.ttl:
                self.queue = deque()
            for item in self.queue:
                if item['args'] == (args, kwargs):
                    self.queue.remove(item)
                    self.queue.appendleft(item)
                    return item['result']
            result = function(*args, **kwargs)
            if len(self.queue) < self.maxsize:
                self.queue.appendleft({'args': (args, kwargs), 'result': result})
            else:
                self.queue.pop()
                self.queue.appendleft({'args': (args, kwargs), 'result': result})
            return result
        self.timestamp = time.time()
        return wrapped
