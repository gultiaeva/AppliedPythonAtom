#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5, n_iter=10000):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        assert regulatization in ('L1', 'L2', None),\
            'Wrong regularization type'
        self.learning_rate = lambda_coef
        self.regularizarion = regulatization
        self.alpha = alpha
        self.iter_num = n_iter

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def loss(self, X, y):
        '''
        Using Mean Absolute Error

        X:(100,3)
        y: (100,1)
        self.__w:(3,1)
        Returns 1D matrix of predictions
        Cost = (y*log(pred) + (1-y)*log(1-pred) ) / len(y)
        '''
        observations = len(y)

        predictions = self.predict(X)
        class1_cost = -y*np.log(predictions)
        class2_cost = (1-y)*np.log(1-predictions)
        cost = class1_cost + class2_cost
        cost = cost.sum() / observations

        return cost

    def update_weights(self, X, y):
        '''
        Vectorized Gradient Descent

        Features:(200, 3)
        Labels: (200, 1)
        Weights:(3, 1)
        '''
        n, m = X.shape
        # 1 - Get Predictions
        predictions = self.predict(X)
        if self.regularizarion == 'L1':
                add = self.alpha * np.ones(m)
                add[0] = 0
        elif self.regularizarion == 'L2':
            add = self.alpha * self.__w * 2
            add[0] = 0
        else:
            add = 0

        # 2 Transpose features from (200, 3) to (3, 200)
        # So we can multiply w the (200,1)  cost matrix.
        # Returns a (3,1) matrix holding 3 partial derivatives --
        # one for each feature -- representing the aggregate
        # slope of the cost function across all observations
        avg_gradient = self.learning_rate * (
            np.dot(X.T,  predictions - y) + add) / n

        # 5 - Subtract from our weights to minimize cost
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
            self.update_weights(X_train, y_train)
            # Calculate error for auditing purposes
            tmp = self.loss(X_train, y_train)
            if np.abs(tmp - cost) < eps:
                cost = tmp
                break
            cost = tmp

        return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
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
        if not all(X_test[:, 0] == 1):
            ones = np.ones((X_test.shape[0], 1))
            X_test = np.hstack([ones, X_test])
        z = np.dot(X_test, self.__w)
        return self._sigmoid(z)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.__w

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}(learning_rate={self.learning_rate}, ' +\
               f'regularization={self.regularizarion}, alpha={self.alpha})'
