#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    A = np.hstack([a, np.eye(a.shape[0])])
    c_basis = np.zeros(a.shape[0])
    basis = np.arange(a.shape[1], A.shape[1])
    c_all = np.hstack([c, c_basis])
    diffs = compute_simplex_diff(A, c_basis, c_all)

    while np.any(diffs > 0):
        j = diffs.argmax()  # координата разрешающего столбца
        jcol = A[:, j]
        tmp = np.divide(b, jcol, where=(jcol > 0))
        # костыль
        # зменяем все, что меньше нуля на бесконечности
        # т.к. необходим минимальный ненулевой элемент
        tmp[tmp <= 0] = np.inf
        i = tmp.argmin()    # координата разрешающей строки
        basis[i] = j        # координаты базисных элементов
        A, b = recalculate_matrix(A, b, i, j)
        c_basis = c_all[basis]
        diffs = compute_simplex_diff(A, c_basis, c_all)

    tmp = np.zeros_like(c_all)
    tmp[basis] = b
    return tmp[:c.shape[0]]


def compute_simplex_diff(A, c_basis, c_all):
    '''
    Метод, вычисляющий симплекс разности
    :param a: np.array, shape=(n, m)
    :param с_basis: np.array, shape=(1, n)
    :param c_all: np.array, shape=(1, m)

    :return: np.array, shape=(1, m)
    '''
    return c_all - c_basis.T @ A


def recalculate_matrix(A, b, r, s):
    '''
    Метод, перечитывающий матрицу на очередном шаге симплекс алгоритма
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(1, n)
    :param r: int, номер разрешающей строки
    :param s: int, номер разрешающего столбца

    :return (A, b): tuple из пересчитанной матрицы и пересчитанных b
    '''
    newA = A.copy()
    newb = b.copy()
    st = np.hstack([newA, newb.reshape((b.shape[0], 1))])
    # st нужен чтобы потом брать из него значения для пересчета
    stacked = st.copy()
    # делим разрешающую строку на разрешающий элемент
    stacked[r] /= stacked[r, s]
    # модифицируем разрешающий столбец
    tmp = stacked[r, s]
    # В лом индексировать все по маске кроме одного
    # проще потом переприсвоить
    stacked[:, s] = 0
    stacked[r, s] = tmp
    for i in np.arange(stacked.shape[0]):
        if i == r:
            continue
        for j in np.arange(stacked.shape[1]):
            if j == s:
                continue
            # разность по диагонали
            stacked[i, j] = st[i, j] - (st[i, s] * st[r, j] / st[r, s])
    return stacked[:, :-1], stacked[:, -1]
