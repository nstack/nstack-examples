#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo.Sink:0.0.1-SNAPSHOT Service
"""
import nstack

class Module(nstack.Module):
    def mylog(self, x):
        print(x)
