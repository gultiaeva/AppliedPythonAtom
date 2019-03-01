#!/usr/bin/env python
# coding: utf-8

from scipy.linalg import det
import numpy as np

def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    if any(len(raw) != len(list_of_lists) for raw in list_of_lists):
        return None
    if len(list_of_lists) == 2:
        return list_of_lists[0][0] * list_of_lists[1][1] - list_of_lists[0][1] * list_of_lists[1][0]
    if len(list_of_lists) == 1:
        return list_of_lists[0][0]
    det = 0
    for i in range(len(list_of_lists)):
        det += (-1)**i * list_of_lists[0][i] * calculate_determinant(
            [[list_of_lists[k][j] for j in range(len(
                list_of_lists)) if j != i] for k in range(len(list_of_lists)) if k != 0]
            )
    return det


matr = [[282.776, 264.011, 291.324],
        [16.077, -222.778, -175.664],
        [143.43, 154.597, -40.907]]


print(calculate_determinant(matr))
# 13810879.339215329