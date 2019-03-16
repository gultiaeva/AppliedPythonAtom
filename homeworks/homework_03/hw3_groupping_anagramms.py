#!/usr/bin/env python
# coding: utf-8
import itertools


def groupping_anagramms(words):
    """
    Функция, которая группирует анаграммы.
    Возвращаем массив, где элементом является массив с анаграмами.
    Пример:  '''Аз есмь строка живу я мерой остр
               За семь морей ростка я вижу рост
               Я в мире сирота
               Я в Риме Ариост'''.split()
                ->
                [
                    ['Аз', 'За'], ['Ариост', 'сирота'],
                    ['Риме', 'мире'], ['Я', 'Я', 'я', 'я'],
                    ['в', 'в'], ['вижу', 'живу'],
                    ['есмь', 'семь'], ['мерой', 'морей'],
                    ['остр', 'рост'], ['ростка', 'строка']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """
    res = []
    for raw_word in words:
        tmp = []
        word = raw_word.lower()
        if len(word) == 1:
            tmp = [word1 for word1 in words if word1.lower() == word]
            if all(set(tmp) != set(perm) for perm in res):
                res.append(tmp)
            continue
        unique_permutations = set(''.join(comb).lower()
                                  for comb in itertools.permutations(word))
        for word1 in words:
            if word1.lower() in unique_permutations:
                tmp.append(word1)
        if all(set(tmp) != set(perm) for perm in res):
            res.append(tmp)
    return res
