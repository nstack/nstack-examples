#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo.DigitString:0.0.1-SNAPSHOT Service
"""
import nstack
import time

class Service(nstack.BaseService):
    def digitString (self, xs):
        return (self.transform(x) for x in xs)
    
    def transform(self, x):
        time.sleep(5) # TODO: Work out how to make this more efficient
        return str(x)

