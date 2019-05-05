#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keras

# keras training callback
# keep all histories for fitting to repeat
# use: fit( initial_epoch=this.initial_epoch(), epochs=this.epoches(epochs), callbacks=[this] ) 
class PersistentHistory(keras.callbacks.Callback):
    def __init__(self):
        super(PersistentHistory, self).__init__()
        self.reset()

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.epoch.append(epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)

    def reset(self):
        self.epoch = []
        self.history = {}

    def initial_epoch(self):
        return len(self.epoch)

    def epochs(self, epochs):
        return epochs + self.initial_epoch()