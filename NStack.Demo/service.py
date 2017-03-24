#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NStack.Demo:0.0.1 Service
"""
import nstack

class Service(nstack.BaseService):
    def numChars(self, x):
        return len(x)

