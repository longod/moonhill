#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = C0111, C0301, C0305, C0326

def safe_cast(value, to_type, default=None):
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default