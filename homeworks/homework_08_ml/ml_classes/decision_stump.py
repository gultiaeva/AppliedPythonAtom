#!/usr/bin/env python
# coding: utf-8

import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        pass

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        assert X.shape[0] == y.shape[0], "shapes don't match"
        X, y = zip(*sorted(zip(X, y), key=lambda x: x[0]))
        X, y = np.array(X), np.array(y)
        hall = np.average(np.square(X - X.mean()))
        n = len(y)
        qs = []
        for i in range(1, n):
            th = ((X[i-1] + X[i]) / 2)[0]
            left, right = X[X < th], X[X > th]
            hleft = np.average(np.square(left - left.mean()))
            hright = np.average(np.square(right - right.mean()))
            q = hall - (len(left) * hleft + len(right) * hright) / n
            qs.append((th, q))

        self.th = max(qs, key=lambda x: x[1])[0]
        self.left = y[(X <= self.th).flatten()].mean()
        self.right = y[(X > self.th).flatten()].mean()

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        return np.array([self.left,
                         self.right])[(X >= self.th).astype('int64')]
