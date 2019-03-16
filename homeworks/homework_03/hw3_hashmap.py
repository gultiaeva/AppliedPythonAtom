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
            if self._key == other._key:
                return True
            return False

        def __str__(self):
            # Проверяем чтобы ключ или значение
            #  не были объектом класса, заданного пользователем
            if type(self._key).__module__ != "builtins":
                k = type(self._key).__name__ + ' object'
            else:
                k = self._key

            if type(self._value).__module__ != "builtins":
                v = type(self._value).__name__ + ' object'
            else:
                v = self._value

            res = f'(Key: {k}; Value: {v})'
            return res

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self._buckets = [None] * bucket_num
        self.tab_len = bucket_num
        self.__n_entries = 0
        self._load_factor = len(self) / self.tab_len

    def get(self, key, default_value=None):
        # Метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        for bucket in self._buckets:
            if bucket is None:
                continue
            for item in bucket:
                if item._key == key:
                    return item._value
        return default_value

    def put(self, key, value):
        # Метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        pos = self._get_index(self._get_hash(key))
        key_in_map = key in self
        if self._buckets[pos] is None:
            self._buckets[pos] = [self.Entry(key, value)]
            self.__n_entries += 1
            self._load_factor = len(self) / self.tab_len
        elif key_in_map:
            for item in self._buckets[pos]:
                if item._key == key:
                    item._value = value
        else:
            self._buckets[pos].append(self.Entry(key, value))
            self.__n_entries += 1
            self._load_factor = len(self) / self.tab_len
        if self._load_factor > 0.67:
            self._resize()

    def __len__(self):
        # Возвращает количество Entry в массиве
        return self.__n_entries

    def _get_hash(self, key):
        # Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # По значению хеша вернуть индекс элемента в массиве
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
        return ((item._key, item._value) for bucket in self._buckets
                if bucket is not None
                for item in bucket)

    def _resize(self):
        # Время от времени нужно ресайзить нашу хешмапу
        # При ресайзе перезаполняем таблицу всеми элементами
        #  т.к. индексы изменились
        tmp_buckets = self._buckets
        self.tab_len = round(self.tab_len * 1.5) + 1
        self._buckets = [None] * self.tab_len
        self.__n_entries = 0
        self._load_factor = len(self) / self.tab_len
        for bucket in tmp_buckets:
            if bucket is None:
                continue
            for item in bucket:
                self.put(item._key, item._value)

    def __str__(self):
        # Метод выводит таблицу в виде
        # [i] -> (key, val) -> ... -> NULL
        res = ''
        for i in range(self.tab_len):
            if self._buckets[i] is None:
                res += f'[{i}] -> NULL\n'
            else:
                res += f'[{i}] -> ' \
                    + ' -> '.join(str(item) for item in self._buckets[i]) \
                    + ' -> NULL\n'

        return res

    def __contains__(self, item):
        # Метод проверяющий есть ли объект (через in)
        pos = self._get_index(self._get_hash(item))

        if self._buckets[pos] is None:
            return False
        for entry in self._buckets[pos]:
            if entry._key == item:
                return True
        return False
