#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return (y_true - y_hat).dot((y_true - y_hat)) / len(y_true)


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return np.sum(np.abs((y_true - y_hat))) / len(y_true)


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    mean_y = y_true.mean()
    Qfact = (y_hat - mean_y).dot((y_hat - mean_y))
    Qall = (y_true - mean_y).dot((y_true - mean_y))
    return Qfact / Qall
