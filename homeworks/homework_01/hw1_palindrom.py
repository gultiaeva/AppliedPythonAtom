#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    if len(input_string) % 2 == 0 and input_string[:len(input_string) // 2] == input_string[:len(input_string) // 2-1:-1]:
        return True
    elif len(input_string) % 2 == 1 and input_string[:len(input_string) // 2] == input_string[:len(input_string) // 2:-1]:
        return True
    else:
        return False
