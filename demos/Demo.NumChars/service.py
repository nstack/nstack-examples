#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo.NumChars:0.0.1 Service
"""
import nstack

class Module(nstack.Module):
    def numChars(self, msg):
        return len(msg)

