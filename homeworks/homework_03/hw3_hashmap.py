#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
    поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self._key = key
            self._value = value

        def get_key(self):
            # Возвращаем ключ
            return self._key

        def get_value(self):
            # Возвращаем значение
            return self._value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            if self._key == other._key:
                return True
            return False

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self._buckets = [None] * bucket_num
        self.tab_len = bucket_num
        self.__n_entries = 0
        self._load_factor = len(self) / len(self._buckets)

    def get(self, key, default_value=None):
        # метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        for bucket in self._buckets:
            if bucket is None:
                continue
            for item in bucket:
                if item._key == key:
                    return item._value
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        try:
            pos = self._get_index(self._get_hash(key))
        except TypeError:
            print('Not added!')
            print('Object is not hashable!')
        else:
            key_in_map = key in self
            if self._buckets[pos] is None and not key_in_map:
                self._buckets[pos] = [self.Entry(key, value)]
                self.__n_entries += 1
                self._load_factor = len(self) / len(self._buckets)
            elif key_in_map:
                for bucket in self._buckets:
                    if bucket is None:
                        continue
                    for item in bucket:
                        if item._key == key:
                            item._value = value
            else:
                self._buckets[pos].append(self.Entry(key, value))
                self.__n_entries += 1
                self._load_factor = len(self) / len(self._buckets)
            if self._load_factor > 0.67:
                self._resize()

    def __len__(self):
        # Возвращает количество Entry в массиве
        return self.__n_entries

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self._buckets)

    def values(self):
        # Должен возвращать итератор значений
        return (item._value for bucket in self._buckets if bucket is not None
                for item in bucket)

    def keys(self):
        # Должен возвращать итератор ключей
        return (item._key for bucket in self._buckets if bucket is not None
                for item in bucket)

    def items(self):
        # Должен возвращать итератор пар ключ и значение (tuples)
        # Для каждого бакета, который не Ноне
        # Для каждого Entry в бакете
        return ((item._key, item._value)
                for bucket in self._buckets if bucket is not None
                for item in bucket)

    def _resize(self):
        # Время от времени нужно ресайзить нашу хешмапу
        self._buckets += [None] * (len(self._buckets) // 2)

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        raise NotImplementedError

    def __contains__(self, item):
        # Метод проверяющий есть ли объект (через in)
        for bucket in self._buckets:
            if bucket is None:
                continue
            for obj in bucket:
                if obj._key == item:
                    return True
        return False
