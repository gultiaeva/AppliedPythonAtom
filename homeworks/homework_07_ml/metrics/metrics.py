#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    class1_cost = -y_true*np.log(y_pred)
    class2_cost = (1-y_true)*np.log(1-y_pred)
    cost = class1_cost + class2_cost
    cost = cost.sum() / len(observations)
    return cost


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return (y_true == y_pred).sum() / len(y_pred)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return (y_pred[y_true == y_pred] == 1).sum() / (y_pred == 1).sum()


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return y_pred[y_true == y_pred].sum() / (y_true == 1).sum()


def fpr(y_true, y_pred):
    """
    false positive rate
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return (y_pred[y_true == 0] == 1).sum() / (y_true == 0).sum()


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    tpr_list = []
    fpr_list = []
    treshold = 0
    for treshold in np.linspace(0, 1, 101):
        tmp = (y_pred >= treshold).astype('int64')
        tpr_list.append(recall(y_true, tmp))
        fpr_list.append(fpr(y_true, tmp))
    roc_auc = np.abs(np.trapz(tpr_list, fpr_list))
    return roc_auc
