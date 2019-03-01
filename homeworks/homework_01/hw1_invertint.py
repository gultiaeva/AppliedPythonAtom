#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if not number:
        return 0
    neg = True if number < 0 else False
    if neg:
        return -int(str(number)[:0:-1])
    else:
        return int(str(number)[::-1])
