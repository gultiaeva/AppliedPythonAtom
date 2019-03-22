#!/usr/bin/env python
# coding: utf-8
import subprocess
from multiprocessing import Pool
import os


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    p = Pool(10)
    files = os.listdir(path_to_dir)
    # Пути относительно cwd
    fullpaths = map(lambda x: f'{path_to_dir}/{x}', files)
    out = p.map(count_words, fullpaths)
    words = {}
    for fn, c in out:
        words[fn] = c
    words['total'] = sum(words.values())
    return words


def count_words(fname):
    cmd = f"cat {fname} | wc -w"
    ps = subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    output = int(ps.communicate()[0].strip())
    return os.path.split(fname)[-1], output
