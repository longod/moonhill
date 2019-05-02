#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GPU Utility for NVIDIA GPU

import os, sys
sys.path.append(os.path.dirname(os.path.abspath('__file__')))
import moonhill.convert

# --help-gpu-query
__query_options = [
    'count',
    'index',
    'name',
    'memory.total',
    'memory.free',
    'memory.used',
    'utilization.gpu',
    'utilization.memory'
]

def query(options=__query_options, id=None, header=False, units=False, exe='nvidia-smi'):
    if options is None:
        return __query_options
    elif type(options) is str:
        opt = options
    elif type(options) is list:
        if len(options) == 0:
            opt = options
        else:
            opt = ','.join(options)
    else:
        raise TypeError('options type must be str or list(str)')
    # no test negative value
    if id is None:
        i = ''
    elif type(id) is int:
        i = '--id={}'.format(str(id))
    else:
        raise TypeError('id type must be None, int')
    noheader = '' if  header else ',noheader'
    nounits = '' if units else ',nounits'
    args = '{} --query-gpu={} --format=csv{}{} {}'.format(exe, opt, noheader, nounits, i)
    import subprocess
    output = subprocess.check_output( args=args, shell=False, universal_newlines=True )
    output = output.strip()
    rows = output.split('\n')
    #print(rows)
    cols =  [ [ moonhill.convert.safe_cast(col, int, col.strip()) for col in row.split(',')] for row in rows ]
    #print(cols)
    if len(cols) == 1:
        if len(cols[0]) == 1:
            return cols[0][0]
        return cols[0]
    return cols

# There is no method of getting current session? or any override current config?

# require tensorflow, optional keras
def memory_allocation_allow_groth(allow_growth=True, with_keras=True):
    import tensorflow
    config = tensorflow.ConfigProto()
    config.gpu_options.allow_growth = allow_growth # pylint: disable=no-member
    # config.visible_device_list considering... but must rename function name
    session = tensorflow.Session(config=config)
    if with_keras:
        import keras.backend
        keras.backend.set_session(session)
    return session

def memory_allocation_fraction(fraction, with_keras=True):
    import tensorflow
    config = tensorflow.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = fraction # pylint: disable=no-member
    session = tensorflow.Session(config=config)
    if with_keras:
        import keras.backend
        keras.backend.set_session(session)
    return session

def memory_allocation_mb(mb, with_keras=True):
    total = query('memory.total')
    fraction = mb / total
    return memory_allocation_fraction(fraction, with_keras=with_keras)

if __name__ == '__main__':
    print(query())
