#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo.Retry:0.0.1-SNAPSHOT Service
"""
import nstack

class Module(nstack.Module):
    def __init__(self):
        self.fail = True

    def faulty_id(self, x):
        if self.fail:
            self.fail = False
            raise RuntimeError("not this time")
        else:
            return x
