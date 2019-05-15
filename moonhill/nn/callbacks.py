#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keras
import matplotlib.pyplot as plt
import numpy

# keras training callbacks

# TODO
# integrate PersistentHistory
# smoothing (Widget)
# text or annotate display option
class HistoryPlotter(keras.callbacks.Callback):
    '''
    Dynamic History Plot for Jupyter
    you must write below
    import matplotlib
    %matplotlib notebook
    '''
    def __init__(self, loss='loss', acc='acc'):
        self.loss = loss
        self.val_loss = 'val_' + loss
        self.acc = acc
        self.val_acc = 'val_' + acc
    def on_train_begin(self, logs=None):
        self.epoch = []
        self.history = {}
        self.figure = plt.figure(figsize=(8,8))
        self.axes_loss = self.figure.add_subplot(2,1,1)
        self.axes_acc = self.figure.add_subplot(2,1,2)

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.epoch.append(epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)
        self.plot()
    
    def plot(self):
        self._plot(self.axes_loss, self.epoch, self.history, self.loss, self.val_loss)
        self._plot(self.axes_acc, self.epoch, self.history, self.acc, self.val_acc)
        self.figure.canvas.draw()

    def _minmax(self, epoch, history):
        min = numpy.argmin(history)
        xmin = epoch[min]
        ymin = numpy.round(history[min], 4)
        max = numpy.argmax(history)
        xmax = epoch[max]
        ymax = numpy.round(history[max], 4)
        return xmin, ymin, xmax, ymax

    def _plot(self, axes, epoch, history, train_y, valid_y):
        axes.clear()
        axes.plot(self.epoch, self.history[train_y], '-', label=train_y)
        xmin, ymin, xmax, ymax = self._minmax(epoch, history[train_y])
        axes.text(xmin, ymin, 'min {}: {}'.format(xmin, ymin), ha = 'right', va = 'top', wrap=True )
        axes.text(xmax, ymax, 'max {}: {}'.format(xmax, ymax), ha = 'left', va = 'bottom', wrap=True )
        if valid_y in history:
            axes.plot(epoch, history[valid_y], '--', label=valid_y)
            xmin, ymin, xmax, ymax = self._minmax(epoch, history[valid_y])
            axes.text(xmin, ymin, 'val min {}: {}'.format(xmin, ymin), ha = 'right', va = 'top', wrap=True )
            axes.text(xmax, ymax, 'val max {}: {}'.format(xmax, ymax), ha = 'left', va = 'bottom', wrap=True )
        axes.relim()
        axes.autoscale_view()
        axes.set_title(train_y)
        axes.legend()

class PersistentHistory(keras.callbacks.Callback):
    '''
    Keep all histories for fitting to repeat
    usage: model.fit( initial_epoch=this.initial_epoch(), epochs=this.epoches(epochs), callbacks=[this] )
    '''
    def __init__(self):
        super(PersistentHistory, self).__init__()
        self.reset()
    def on_train_begin(self, logs=None):
        self.last_initial_epoch = self.initial_epoch()

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.epoch.append(epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)

    def reset(self):
        self.epoch = []
        self.history = {}
        self.last_initial_epoch = self.initial_epoch()

    def initial_epoch(self):
        return len(self.epoch)

    def epochs(self, epochs):
        return epochs + self.initial_epoch()

    def last_trained_epoch(self):
        return self.initial_epoch() - len(self.epoch)
