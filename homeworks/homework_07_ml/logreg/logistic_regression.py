#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regularization=None, alpha=0.5, n_iter=10000):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        assert regularization in ('L1', 'L2', None),\
            'Wrong regularization type'
        self.learning_rate = lambda_coef
        self.regularizarion = regularization
        self.alpha = alpha
        self.iter_num = n_iter

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def loss(self, X, y):
        '''

        X: matrix of n objects & m features for each
        y: vector of true labels
        Returns 1D matrix of predictions
        Cost = (y*log(pred) + (1-y)*log(1-pred) ) / len(y)
        '''

        predictions = self.predict_proba(X)[:, 1]
        class1_cost = -y * np.log(predictions)
        class2_cost = (1 - y) * np.log(1 - predictions)
        cost = class1_cost + class2_cost
        cost = cost.sum() / len(y)

        return cost

    def _update_weights(self, X, y):
        '''
        Updates weigsts using gradient descent

        X: matrix of n objects & m features for each
        y: vector of true labels
        '''
        n, m = X.shape
        # Get Predictions
        predictions = self.predict_proba(X)[:, 1]
        # Provide L1 & L2 regularization
        if self.regularizarion == 'L1':
                add = self.alpha * np.ones(m)
                add[0] = 0
        elif self.regularizarion == 'L2':
            add = self.alpha * self.__w * 2
            add[0] = 0
        else:
            add = 0

        # Calculate step for gradient descent
        avg_gradient = self.learning_rate * (
            np.dot(X.T,  predictions - y) + add) / n

        # Subtract from weights to minimize cost
        self.__w -= avg_gradient

    def fit(self, X_train, y_train, eps=1e-6):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        self.__fitted = True
        assert X_train.shape[0] == y_train.shape[0], "Shapes don't match"
        ones = np.ones((X_train.shape[0], 1))
        X_train = np.hstack([ones, X_train])
        n, m = X_train.shape
        self.__w = np.random.randn(m)
        cost = np.inf

        for i in range(self.iter_num):
            self._update_weights(X_train, y_train)
            # Calculate error for auditing purposes
            tmp = self.loss(X_train, y_train)
            if np.abs(tmp - cost) < eps:
                cost = tmp
                break
            cost = tmp
        self.intercept_ = self.__w[0]
        self.coef_ = self.__w[1:]
        return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self.__fitted, 'Model is not fitted'
        if not all(X_test[:, 0] == 1):
            ones = np.ones((X_test.shape[0], 1))
            X_test = np.hstack([ones, X_test])
        z = np.dot(X_test, self.__w)
        return (self._sigmoid(z) >= 0.5).astype('int64')

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        assert self.__fitted, 'Model is not fitted'
        if not all(X_test[:, 0] == 1):
            ones = np.ones((X_test.shape[0], 1))
            X_test = np.hstack([ones, X_test])
        z = np.dot(X_test, self.__w)
        res = self._sigmoid(z)
        return np.column_stack([1 - res, res])

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert self.__fitted, 'Model is not fitted'
        return self.__w

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}(learning_rate={self.learning_rate}, ' +\
               f'regularization={self.regularizarion}, alpha={self.alpha}, ' +\
               f'n_iterations={self.iter_num})'
