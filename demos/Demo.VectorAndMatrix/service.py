#!/usr/bin/env python3
"""
Demo.VectorAndMatrix:0.0.1-SNAPSHOT Service
"""
import nstack

class Service(nstack.BaseService):
    def matrixTo2(self, x):
        return len(x)

    def vectorTo5(self, x):
        return len(x)

