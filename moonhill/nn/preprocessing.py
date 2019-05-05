#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import sklearn.base

# sklearn 非依存もあったほうがいいかも

# standardization
class StandardizationScaler(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    def __init__(self):
        self.__std = 1
        self.__mean = 0

    def fit(self, X, y=None):
        self.__std = X.std()
        self.__mean = X.mean()
        return self

    def transform(self, X):
        # 除算を* 1/nを事前に用意しておくと誤差で微妙に結果が異なる
        n = (X - self.__mean) / self.__std # possible ZeroDivisionError
        return n

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)

    def inverse_transform(self, X):
        n = X * self.__std + self.__mean
        return n

# normalization -1 to 1
class NormalizationScaler(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    def __init__(self):
        self.__norm = 1
        pass

    def fit(self, X, y=None):
        self.__norm = numpy.amax( numpy.abs(X) )
        return self

    def transform(self, X):
        # 除算を* 1/nを事前に用意しておくと誤差で微妙に結果が異なる
        n = X / self.__norm # possible ZeroDivisionError
        return n

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)

    def inverse_transform(self, X):
        n = X * self.__norm
        return n
