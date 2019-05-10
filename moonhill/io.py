#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

def read_text(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding) as fp:
        data = fp.read()
        fp.close()
    return data

def write_text(path, data, encoding='utf-8'):
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w', encoding=encoding) as fp:
        fp.write(data)
        fp.close()
