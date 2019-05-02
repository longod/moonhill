#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

def read_text(path, encoding='utf-8'):
    fp = open(path, 'r', encoding=encoding)
    data = fp.read()
    fp.close()
    return data

def write_text(path, data, encoding='utf-8'):
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    fp = open(path, 'w', encoding=encoding)
    fp.write(data)
    fp.close()

def read_json(path):
    data = read_text(path, 'utf-8')
    return json.loads(data)

def write_json(path, data, sort_keys=False):
    j = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=sort_keys)
    write_text(path, j, 'utf-8')
