#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keras

# Functional, Sequentialの切り替えは？

# input_shape=(227,1)
def alexnet_1d(model=None):
    if model is None:
        model = keras.models.Sequential()
    model.add(keras.layers.Conv1D(filters=48, kernel_size=11, strides=4,  activation='relu', padding='valid' ))
    model.add(keras.layers.MaxPooling1D(pool_size=3, strides=2, padding='same'))
    #model.add(keras.layers.BatchNormalization()) # instad of Local Response Normalization (k=2, n=5, alpha=10-4, beta=0.75)

    model.add(keras.layers.Conv1D(filters=128, kernel_size=5, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=3, strides=2, padding='same'))
    #model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Conv1D(filters=192, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=192, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=3, strides=2, padding='same'))
    #model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(4096, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(4096, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    return model


# input_shape=(224,1)
def vgg16_1d(model=None):
    if model is None:
        model = keras.models.Sequential()
    model = keras.models.Sequential()
    model.add(keras.layers.Conv1D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=2, strides=2, padding='same'))

    model.add(keras.layers.Conv1D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=2, strides=2, padding='same'))

    model.add(keras.layers.Conv1D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=2, strides=2, padding='same'))

    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=2, strides=2, padding='same'))

    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.Conv1D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling1D(pool_size=2, strides=2, padding='same'))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(4096, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(4096, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    return model