#!/usr/bin/env python
# coding: utf-8

from metrics import *


class LinearRegression:
    def __init__(self, lambda_coef=0.1, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        assert regulatization in ('L1', 'L2', None)
        self.learning_rate = lambda_coef
        self.regularizarion = regulatization
        self.alpha = alpha

    def fit(self, X_train, y_train, iterations=1000, eps=1e-6):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        ones = np.ones((X_train.shape[0], 1))
        X_train = np.hstack([ones, X_train])
        n, m = X_train.shape
        cost_history = np.zeros(iterations)
        self.__w = np.random.randn(m) / np.sqrt(m)
        for it in range(iterations):
            if self.regularizarion == 'L1':
                add = self.alpha * np.ones(m) / 2
            elif self.regularizarion == 'L2':
                add = self.alpha * self.__w
            else:
                add = 0
            prediction = self.predict(X_train)
            self.__w -= (2/n) * self.learning_rate*(X_train.T.dot((prediction - y_train)) + add)
            cost_history[it] = mse(y_train, prediction)
            if it and abs(cost_history[it] - cost_history[it-1]) < eps:
                break
        self.coef_ = self.__w[1:]
        self.intercept_ = self.__w[0]
        return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if all(X_test[:, 0] == 1):
            return X_test.dot(self.__w)
        else:
            ones = np.ones((X_test.shape[0], 1))
            X_test = np.hstack([ones, X_test])
            return X_test.dot(self.__w)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.__w

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}(learning_rate={self.learning_rate}, '\
               f'regularization={self.regularizarion}, alpha={self.alpha})'
